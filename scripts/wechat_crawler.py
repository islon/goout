import json
import os
import re
import time
import random
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    SELENIUM_AVAILABLE = True
except ImportError:
    SELENIUM_AVAILABLE = False

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
}

SOGOU_BASE_URL = 'https://weixin.sogou.com/weixin'
BAIDU_BASE_URL = 'https://www.baidu.com/s'


def clean_text(text):
    if not text:
        return ''
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    text = text.replace('\u3000', ' ').replace('\xa0', ' ')
    return text


def parse_date(date_str):
    date_str = clean_text(date_str)
    if not date_str:
        return None
    
    today = datetime.now().date()
    
    if '今天' in date_str or '今日' in date_str:
        return today
    if '昨天' in date_str or '昨日' in date_str:
        return (today - timedelta(days=1))
    if '前天' in date_str:
        return (today - timedelta(days=2))
    if '小时前' in date_str:
        return today
    if '分钟前' in date_str:
        return today
    
    month_match = re.search(r'(\d+)月(\d+)日', date_str)
    if month_match:
        month = int(month_match.group(1))
        day = int(month_match.group(2))
        year = today.year
        if month > today.month:
            year -= 1
        try:
            return datetime(year, month, day).date()
        except:
            pass
    
    date_match = re.search(r'(\d{4})[-/年](\d{1,2})[-/月](\d{1,2})[日号]?', date_str)
    if date_match:
        try:
            return datetime(
                int(date_match.group(1)),
                int(date_match.group(2)),
                int(date_match.group(3))
            ).date()
        except:
            pass
    
    return None


class WeChatCrawler:
    def __init__(self, headless=True, timeout=30):
        self.headless = headless
        self.timeout = timeout
        self.driver = None
    
    def _init_driver(self):
        if not SELENIUM_AVAILABLE:
            raise RuntimeError("selenium not installed. Install with: pip install selenium")
        
        options = Options()
        if self.headless:
            options.add_argument('--headless=new')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-infobars')
        options.add_argument('--disable-extensions')
        options.add_argument(f'user-agent={HEADERS["User-Agent"]}')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_page_load_timeout(self.timeout)
        self.driver.set_script_timeout(self.timeout)
    
    def _close_driver(self):
        if self.driver:
            try:
                self.driver.quit()
            except:
                pass
            self.driver = None
    
    def search_by_account(self, account_name, max_results=10):
        results = []
        query = self._clean_query(account_name)
        
        try:
            results.extend(self._sogou_search(query, account=True, max_results=max_results))
            if not results:
                results.extend(self._baidu_search(query, max_results=max_results))
        except Exception as e:
            print(f"搜索公众号失败: {account_name}, 错误: {e}")
        
        return list({r['url']: r for r in results}.values())[:max_results]
    
    def _clean_query(self, query):
        query = clean_text(query)
        query = query.replace('公众号', '').replace('官方', '')
        return query
    
    def _sogou_search(self, query, account=False, max_results=10):
        results = []
        try:
            params = {
                'query': query,
                'type': '1' if account else '2',
                'ie': 'utf8',
            }
            response = requests.get(SOGOU_BASE_URL, params=params, headers=HEADERS, timeout=15)
            soup = BeautifulSoup(response.text, 'lxml')
            
            if account:
                for item in soup.select('.news-list li')[:max_results]:
                    account_link = item.select_one('a[uigs*="account_name"]')
                    if account_link:
                        account_url = account_link.get('href')
                        if account_url and 'mp.weixin.qq.com' in account_url:
                            results.append({
                                'title': clean_text(account_link.get_text()),
                                'url': account_url,
                                'source': '搜狗微信搜索',
                            })
            else:
                for item in soup.select('.news-list li')[:max_results]:
                    title_tag = item.select_one('h3 a')
                    summary_tag = item.select_one('.txt-info')
                    date_tag = item.select_one('.s2')
                    if title_tag:
                        results.append({
                            'title': clean_text(title_tag.get_text()),
                            'url': title_tag.get('href'),
                            'summary': clean_text(summary_tag.get_text()) if summary_tag else '',
                            'date': parse_date(date_tag.get_text()) if date_tag else None,
                            'source': '搜狗微信搜索',
                        })
        except Exception as e:
            print(f"搜狗搜索失败: {e}")
        
        return results
    
    def _baidu_search(self, query, max_results=10):
        results = []
        try:
            params = {
                'wd': f'{query} 微信公众号',
                'tn': 'baidurt',
            }
            response = requests.get(BAIDU_BASE_URL, params=params, headers=HEADERS, timeout=15)
            soup = BeautifulSoup(response.text, 'lxml')
            
            for item in soup.select('.result.c-container')[:max_results]:
                title_tag = item.select_one('h3 a')
                link_tag = item.select_one('a')
                abstract_tag = item.select_one('.c-abstract')
                if link_tag:
                    href = link_tag.get('href')
                    if href and 'mp.weixin.qq.com' in href:
                        results.append({
                            'title': clean_text(title_tag.get_text()) if title_tag else '',
                            'url': href,
                            'summary': clean_text(abstract_tag.get_text()) if abstract_tag else '',
                            'source': '百度搜索',
                        })
        except Exception as e:
            print(f"百度搜索失败: {e}")
        
        return results
    
    def fetch_articles_from_account(self, account_url, max_articles=20, days_back=30):
        articles = []
        if not account_url or 'mp.weixin.qq.com' not in account_url:
            return articles
        
        try:
            if not self.driver:
                self._init_driver()
            
            self.driver.get(account_url)
            time.sleep(3)
            
            try:
                cookie_btn = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '.weui-popup__close-btn'))
                )
                cookie_btn.click()
            except:
                pass
            
            article_elements = self.driver.find_elements(By.CSS_SELECTOR, 'a[data-report-click]')
            today = datetime.now().date()
            
            for idx, elem in enumerate(article_elements[:max_articles]):
                try:
                    title = elem.get_attribute('title') or elem.text
                    url = elem.get_attribute('href')
                    
                    if url and 'mp.weixin.qq.com' in url:
                        articles.append({
                            'title': clean_text(title),
                            'url': url,
                            'order': idx,
                        })
                except:
                    continue
            
            self._close_driver()
        except Exception as e:
            print(f"获取公众号文章失败: {e}")
            self._close_driver()
        
        return articles
    
    def fetch_article_content(self, article_url):
        content = {
            'title': '',
            'date': None,
            'author': '',
            'content': '',
            'url': article_url,
            'success': False,
        }
        
        if not article_url or 'mp.weixin.qq.com' not in article_url:
            return content
        
        try:
            if not self.driver:
                self._init_driver()
            
            self.driver.get(article_url)
            time.sleep(3)
            
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.rich_media_title'))
                )
            except:
                pass
            
            title_elem = self.driver.find_element(By.CSS_SELECTOR, '.rich_media_title')
            content['title'] = clean_text(title_elem.text)
            
            date_elem = self.driver.find_element(By.CSS_SELECTOR, '#publish_time')
            content['date'] = parse_date(date_elem.text)
            
            author_elem = self.driver.find_element(By.CSS_SELECTOR, '.rich_media_meta .rich_media_meta_text')
            content['author'] = clean_text(author_elem.text)
            
            content_elem = self.driver.find_element(By.CSS_SELECTOR, '.rich_media_content')
            content['content'] = clean_text(content_elem.text)
            
            content['success'] = True
            self._close_driver()
        except Exception as e:
            print(f"获取文章内容失败: {article_url}, 错误: {e}")
            self._close_driver()
        
        return content


def crawl_wechat_articles(account_names, max_articles_per_account=10, days_back=30):
    crawler = WeChatCrawler(headless=True)
    all_articles = []
    
    for account_name in account_names:
        print(f"正在爬取公众号: {account_name}")
        try:
            accounts = crawler.search_by_account(account_name)
            if accounts:
                account_url = accounts[0]['url']
                articles = crawler.fetch_articles_from_account(account_url, max_articles=max_articles_per_account)
                
                for article in articles:
                    content = crawler.fetch_article_content(article['url'])
                    if content['success']:
                        content['account_name'] = account_name
                        all_articles.append(content)
                        print(f"  ✓ 获取文章: {content['title']}")
                    else:
                        print(f"  ✗ 获取文章失败: {article['title']}")
        except Exception as e:
            print(f"爬取公众号失败: {account_name}, 错误: {e}")
        
        time.sleep(random.uniform(1, 3))
    
    return all_articles


if __name__ == "__main__":
    test_accounts = ["深圳博物馆", "深圳音乐厅", "深圳市文化馆"]
    articles = crawl_wechat_articles(test_accounts, max_articles_per_account=3)
    print(f"\n共获取 {len(articles)} 篇文章")
    for article in articles:
        print(f"- {article['title']} | {article['date']} | {article['account_name']}")
