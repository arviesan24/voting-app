Vue.options.delimiters = ['[[', ']]'];
Vue.config.debug = vueDebug;
var vm = new Vue({
    el: '.app',
    data: {
      choices: null,
      dropdownOptions: [],
      selectedChoice: Number
    },
    mounted() {
      axios.get(`${API_ROOT_URL}choices/?poll=${pollId}`)
      .then(response => {
        this.$nextTick(() => {
          this.choices = response.data;
          this.choices.forEach(choice => {
            this.dropdownOptions.push({
              value: choice.id,
              name: choice.name
            });
          });
        });
      })
    },
    methods: {
      saveVote(choice) {
        // get the selected value that will be passed to the post request.
        this.selectedChoice = choice;
      }
    }
  })
