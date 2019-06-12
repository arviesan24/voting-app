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
      this.loadChart();
    },
    methods: {
      loadChart() {
        axios.get(`${API_ROOT_URL}choices/?poll=${pollId}`)
        .then(response => {
          this.$nextTick(() => {
            this.choices = response.data;
            this.selectedChoice = this.choices[0].id;
            this.choices.forEach(choice => {
              this.dropdownOptions.push({
                value: choice.id,
                name: choice.name
              });
            });
          });
        })
      },
      getVote(choice) {
        // get the selected value that will be passed to the post request.
        this.selectedChoice = Number(choice);
      },
      saveVote() {
        axios.defaults.xsrfCookieName = 'csrftoken';
        axios.defaults.xsrfHeaderName = 'X-CSRFToken';
        axios.post(`${API_ROOT_URL}votes/`, {content_type: 'choice', object_id: this.selectedChoice})
        .then((response) => {
          // reinitialize the values and reload chart.
          this.choices = null
          this.dropdownOptions = []
          this.selectedChoice = null
          this.loadChart();
        });
      }
    }
  })
