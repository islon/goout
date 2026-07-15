import json
import os
import re
import sys
from datetime import datetime, timedelta
from typing import List, Dict, Optional

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

try:
    from anthropic import Anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False

CATEGORY_KEYWORDS = {
    '展览': ['展', '展览', '博览会', '艺术展', '书画展', '摄影展', '特展', '沉浸展', '珍品展'],
    '讲座阅读': ['讲座', '沙龙', '分享会', '读书', '阅读', '绘本', '故事会', '论坛', '朗诵', '书海', '参访'],
    '科普活动': ['科普', '科学', '实验', '机器人', '编程', '科技', '天文', '探索', 'AI', '科技馆'],
    '演出': ['音乐会', '歌剧', '话剧', '戏曲', '舞蹈', '演唱会', '演出', '音乐剧', '儿童剧', '演奏', '剧场'],
    '体育赛事': ['足球', '篮球', '羽毛球', '乒乓球', '网球', '马拉松', '比赛', '赛事', '体育', '中超'],
    '亲子活动': ['亲子', '儿童', '少儿', '宝宝', '家庭', '手工', '烘焙', '暑期', '非遗', '体验'],
    '影视放映': ['电影', '放映', '观影', '书影'],
}

VENUE_KEYWORDS = {
    '深圳图书馆': ['深圳图书馆', '深图'],
    '深圳少年儿童图书馆': ['少儿图书馆', '少年儿童图书馆'],
    '深圳博物馆': ['深圳博物馆', '深博'],
    '深圳科学技术馆': ['深圳科技馆', '光明科技馆', '科学技术馆'],
    '深圳市少年宫': ['少年宫'],
    '深圳滨海艺术中心': ['滨海艺术中心'],
    '深圳音乐厅': ['深圳音乐厅', '音乐厅'],
    '深圳市文化馆': ['深圳市文化馆', '市文化馆'],
    '南山图书馆': ['南山图书馆', '南图'],
    '宝安图书馆': ['宝安图书馆'],
    '福田区图书馆': ['福田图书馆'],
    '罗湖区图书馆': ['罗湖图书馆'],
    '龙岗区图书馆': ['龙岗图书馆'],
    '龙华区图书馆': ['龙华图书馆'],
    '光明区图书馆': ['光明区图书馆', '光明图书馆'],
    '坪山区图书馆': ['坪山图书馆'],
    '盐田区图书馆': ['盐田图书馆'],
    '大鹏新区图书馆': ['大鹏图书馆'],
    '南山博物馆': ['南山博物馆'],
    '龙岗区博物馆': ['龙岗博物馆'],
    '宝安区博物馆': ['宝安博物馆'],
    '宝安科技馆': ['宝安科技馆'],
    '龙岗区科技馆': ['龙岗科技馆'],
    '龙华区科技馆': ['龙华科技馆'],
    '宝安区青少年宫': ['宝安青少年宫'],
    '南山区青少年活动中心': ['南山青少年活动中心'],
    '龙岗区青少年宫': ['龙岗青少年宫'],
    '龙华区青少年宫': ['龙华青少年宫'],
    '宝安体育中心': ['宝安体育中心'],
    '南山文体中心': ['南山文体中心'],
    '深圳湾体育中心': ['深圳湾体育中心'],
    '深圳市体育中心': ['深圳市体育中心', '市体育中心'],
}

FEE_KEYWORDS = {
    '免费': ['免费', '公益', '不收费', '免票', '免费入场'],
    '免费需预约': ['免费', '预约', '抢票', '报名', '名额有限'],
    '收费': ['收费', '票价', '购票', '门票', '元', '购票链接'],
}


def parse_date_range(text: str) -> tuple:
    today = datetime.now().date()
    
    date_patterns = [
        r'(\d{4})年(\d{1,2})月(\d{1,2})日\s*[至到]\s*(\d{4})年(\d{1,2})月(\d{1,2})日',
        r'(\d{1,2})月(\d{1,2})日\s*[至到]\s*(\d{1,2})月(\d{1,2})日',
        r'(\d{1,2})月(\d{1,2})日\s*-\s*(\d{1,2})月(\d{1,2})日',
        r'(\d{4})[-/](\d{1,2})[-/](\d{1,2})\s*[至到]\s*(\d{4})[-/](\d{1,2})[-/](\d{1,2})',
        r'(\d{1,2})[-/](\d{1,2})\s*[至到]\s*(\d{1,2})[-/](\d{1,2})',
        r'(\d{4})[-/](\d{1,2})[-/](\d{1,2})\s*-\s*(\d{1,2})[-/](\d{1,2})',
        r'(\d{4})年(\d{1,2})月(\d{1,2})日',
        r'(\d{1,2})月(\d{1,2})日',
        r'(\d{4})[-/](\d{1,2})[-/](\d{1,2})',
    ]
    
    for pattern in date_patterns:
        match = re.search(pattern, text)
        if match:
            groups = match.groups()
            try:
                if len(groups) == 6:
                    start_date = datetime(int(groups[0]), int(groups[1]), int(groups[2])).date()
                    end_date = datetime(int(groups[3]), int(groups[4]), int(groups[5])).date()
                    return start_date, end_date
                elif len(groups) == 4:
                    year = today.year
                    if pattern in date_patterns[:3]:
                        start_date = datetime(year, int(groups[0]), int(groups[1])).date()
                        end_date = datetime(year, int(groups[2]), int(groups[3])).date()
                    else:
                        year = int(groups[0]) if len(groups[0]) == 4 else today.year
                        month = int(groups[1])
                        start_date = datetime(year, month, int(groups[2])).date()
                        end_date = datetime(year, month, int(groups[3])).date()
                    return start_date, end_date
                elif len(groups) == 3:
                    year = int(groups[0]) if len(groups[0]) == 4 else today.year
                    month = int(groups[1])
                    day = int(groups[2])
                    date = datetime(year, month, day).date()
                    return date, date
                elif len(groups) == 2:
                    year = today.year
                    date = datetime(year, int(groups[0]), int(groups[1])).date()
                    return date, date
            except:
                continue
    
    return None, None


def extract_venue(text: str) -> str:
    for venue, keywords in VENUE_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text:
                return venue
    return ''


def extract_category(text: str) -> str:
    for category, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text:
                return category
    return '其他'


def extract_fee(text: str) -> str:
    has_free = any(kw in text for kw in FEE_KEYWORDS['免费'])
    has_reserve = any(kw in text for kw in FEE_KEYWORDS['免费需预约'])
    has_charge = any(kw in text for kw in FEE_KEYWORDS['收费'])
    
    if has_charge and not has_free:
        return '收费'
    elif has_free and has_reserve:
        return '免费需预约'
    elif has_free:
        return '免费'
    return '免费'


def is_family_friendly(text: str) -> bool:
    family_keywords = ['亲子', '儿童', '少儿', '宝宝', '家庭', '暑期', '夏令营', '小朋友']
    return any(kw in text for kw in family_keywords)


def rule_based_parse(article: Dict) -> List[Dict]:
    activities = []
    
    content = article.get('content', '') + article.get('title', '')
    title = article.get('title', '')
    url = article.get('url', '')
    account_name = article.get('account_name', '')
    publish_date = article.get('date')
    
    start_date, end_date = parse_date_range(content)
    
    if not start_date:
        if publish_date:
            start_date = publish_date
            end_date = publish_date + timedelta(days=30)
    
    if not start_date:
        return activities
    
    venue = extract_venue(content) or extract_venue(account_name)
    category = extract_category(content)
    fee = extract_fee(content)
    family_friendly = is_family_friendly(content)
    
    if venue and category != '其他':
        activities.append({
            'title': title,
            'venue': venue,
            'start_date': start_date.strftime('%Y-%m-%d'),
            'end_date': end_date.strftime('%Y-%m-%d') if end_date else start_date.strftime('%Y-%m-%d'),
            'link': url,
            'description': content[:500],
            'category': category,
            'fee': fee,
            'contact': '',
            'family_friendly': family_friendly,
            'source': f'微信公众号-{account_name}',
        })
    
    return activities


def llm_parse(article: Dict, api_key: str = None) -> List[Dict]:
    if not api_key:
        return rule_based_parse(article)
    
    content = article.get('content', '')
    title = article.get('title', '')
    url = article.get('url', '')
    account_name = article.get('account_name', '')
    
    if len(content) > 3000:
        content = content[:3000]
    
    prompt = f"""
你是一个活动信息提取专家。请从以下微信公众号文章内容中提取深圳公立场馆的活动信息。

文章标题: {title}
文章来源: {account_name}

文章内容:
{content}

请提取所有活动信息，每个活动输出为JSON对象，包含以下字段：
- title: 活动名称（简短）
- venue: 场馆名称（从以下列表选择：{', '.join(VENUE_KEYWORDS.keys())}）
- start_date: 开始日期（格式YYYY-MM-DD）
- end_date: 结束日期（格式YYYY-MM-DD）
- link: 文章链接（使用提供的URL）
- description: 活动描述（不超过100字）
- category: 活动分类（从以下选择：展览, 讲座阅读, 科普活动, 演出, 体育赛事, 亲子活动, 影视放映）
- fee: 收费情况（免费/免费需预约/收费）
- contact: 联系方式（电话号码或邮箱）
- family_friendly: 是否适合亲子（true/false）
- source: 数据来源（格式：微信公众号-来源名称）

重要规则：
1. 只提取真实存在的活动，不要虚构
2. 如果文章中没有明确的活动信息，返回空数组
3. 如果无法确定某个字段，留空或使用合理默认值
4. 只提取未来1-2个月内的活动
5. 商业培训、付费课程等非公益内容不要提取

请以JSON数组格式输出，不要包含任何其他文字。
"""
    
    try:
        if OPENAI_AVAILABLE and api_key.startswith('sk-'):
            openai.api_key = api_key
            response = openai.ChatCompletion.create(
                model='gpt-4o-mini',
                messages=[{'role': 'user', 'content': prompt}],
                temperature=0.1,
            )
            result = response.choices[0].message.content
        elif ANTHROPIC_AVAILABLE:
            client = Anthropic(api_key=api_key)
            response = client.messages.create(
                model='claude-3-haiku-20240307',
                max_tokens=2000,
                messages=[{'role': 'user', 'content': prompt}],
            )
            result = response.content[0].text
        else:
            return rule_based_parse(article)
        
        result = result.strip()
        if not result.startswith('['):
            result = '[' + result
        if not result.endswith(']'):
            result = result + ']'
        
        activities = json.loads(result)
        
        for activity in activities:
            activity['link'] = url
            activity['source'] = f'微信公众号-{account_name}'
        
        return activities
    except Exception as e:
        print(f"LLM解析失败: {e}")
        return rule_based_parse(article)


def analyze_articles(articles: List[Dict], api_key: str = None, use_llm: bool = True) -> List[Dict]:
    all_activities = []
    
    for article in articles:
        if use_llm and api_key:
            activities = llm_parse(article, api_key)
        else:
            activities = rule_based_parse(article)
        
        for activity in activities:
            activity['article_title'] = article.get('title', '')
            activity['article_date'] = article.get('date').strftime('%Y-%m-%d') if article.get('date') else ''
            all_activities.append(activity)
    
    return all_activities


if __name__ == "__main__":
    test_article = {
        'title': '深圳博物馆暑期延时开放公告',
        'content': '深圳博物馆将于2026年7月1日至8月31日实施暑期延时开放。延时期间，金田路馆与同心路馆开放时间延长至21:00（20:30停止入场），改革开放展览馆开放时间为10:00-21:00。暑期延时开放期间，观众可免费预约参观。',
        'url': 'https://mp.weixin.qq.com/s/test',
        'account_name': '深圳博物馆',
        'date': datetime.now().date(),
    }
    
    activities = analyze_articles([test_article], use_llm=False)
    print(f"提取到 {len(activities)} 个活动")
    for activity in activities:
        print(json.dumps(activity, ensure_ascii=False, indent=2))
