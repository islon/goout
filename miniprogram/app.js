App({
  onLaunch() {
    // 云开发初始化
    // 用户开通云开发后，将 env 替换为实际的环境 ID
    if (wx.cloud) {
      wx.cloud.init({
        env: 'goout-prod',  // 替换为你的云开发环境ID
        traceUser: true
      })
    }
  },
  globalData: {
    userInfo: null
  }
})
