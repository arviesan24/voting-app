Vue.options.delimiters = ['[[', ']]'];
Vue.config.debug = vueDebug;
var vm = new Vue({
  el: '.app',
  data: {
    choices: []
  },
  mounted() {
    this.loadChoices();
  },
  methods: {
    loadChoices() {
      axios.get(`${API_ROOT_URL}choices/?poll=${pollId}`)
      .then(response => {
        this.choices = response.data;
        console.log(this.choices);
      });
    }
  },
});
