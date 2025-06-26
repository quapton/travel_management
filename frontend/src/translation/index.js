export default {
  install(app) {
    // You can customize this
    app.config.globalProperties.$t = (key) => key
  }
}
