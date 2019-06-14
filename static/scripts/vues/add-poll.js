Vue.options.delimiters = ['[[', ']]'];
Vue.config.debug = vueDebug;
var vm = new Vue({
  el: '#app',
  data: {
    showModal: false,
    newPoll: {}
  },
  methods: {
    getNewPoll(e) {
      this.newPoll = e;
    }
  },
})
