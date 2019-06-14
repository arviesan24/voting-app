Vue.options.delimiters = ['[[', ']]'];
Vue.config.debug = vueDebug;
var vm = new Vue({
  el: '.app',
  data: {
    choices: [],
    showModal: false,
    selectedChoice: {}
  },
  mounted() {
    this.loadChoices();
  },
  methods: {
    loadChoices() {
      axios.get(`${API_ROOT_URL}choices/?poll=${pollId}`)
      .then(response => {
        this.choices = response.data;
      });
    },
    selectedChoiceValue(e) {
      this.showModal = true;
      this.selectedChoice = e;
    }
  },
});
