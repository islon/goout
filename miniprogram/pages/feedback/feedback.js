// 童行小程序 - 反馈页
const GITHUB_ISSUES_URL = 'https://github.com/islon/goout/issues';

Page({
  data: {
    categories: [
      { key: 'data', name: '数据报错', desc: '活动/场馆信息错误' },
      { key: 'feature', name: '功能建议', desc: '希望小程序增加什么' },
      { key: 'venue', name: '场馆补充', desc: '想新增/完善场馆' },
      { key: 'other', name: '其他', desc: '任何问题或建议' }
    ],
    category: 'data',
    content: '',
    target: ''
  },

  onLoad(options) {
    const type = options.type || 'other';
    const target = decodeURIComponent(options.target || '');
    const categoryMap = {
      venue: 'venue',
      activity: 'data',
      data: 'data',
      feature: 'feature',
      other: 'other'
    };
    let content = '';
    if (target) {
      content = '反馈对象：' + target + '\n';
    }
    this.setData({
      category: categoryMap[type] || 'other',
      target: target,
      content: content
    });
  },

  onCategoryTap(e) {
    this.setData({ category: e.currentTarget.dataset.key });
  },

  onContentInput(e) {
    this.setData({ content: e.detail.value });
  },

  buildFeedbackText() {
    const categoryName = this.getCategoryName(this.data.category);
    let text = '【反馈类型】' + categoryName + '\n';
    if (this.data.target) {
      text += '【反馈对象】' + this.data.target + '\n';
    }
    text += '【反馈内容】\n' + (this.data.content || '（未填写）') + '\n';
    text += '【来自】童行小程序\n';
    return text;
  },

  getCategoryName(key) {
    for (let i = 0; i < this.data.categories.length; i++) {
      if (this.data.categories[i].key === key) {
        return this.data.categories[i].name;
      }
    }
    return '其他';
  },

  onCopyFeedback() {
    if (!this.data.content.trim()) {
      wx.showToast({ title: '请先填写反馈内容', icon: 'none' });
      return;
    }
    wx.setClipboardData({
      data: this.buildFeedbackText(),
      success: () => {
        wx.showModal({
          title: '已复制反馈',
          content: '你可以直接粘贴到下方的「微信反馈」中提交给管理员。',
          showCancel: false,
          confirmText: '知道了'
        });
      }
    });
  },

  onCopyGitHub() {
    wx.setClipboardData({
      data: GITHUB_ISSUES_URL,
      success: () => wx.showToast({ title: 'GitHub 链接已复制', icon: 'success' })
    });
  }
});
