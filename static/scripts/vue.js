Vue.options.delimiters = ['[[', ']]'];
Vue.config.debug = vueDebug;
var vm = new Vue({
    el: '.app',
    data: {
      choices: null,
      dropdownOptions: []
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
    }
  })
