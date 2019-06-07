Vue.options.delimiters = ['[[', ']]'];

var vm = new Vue({
    el: '.app',
    data: {
      choices: {}
    },
    mounted() {
      axios.get(`${API_ROOT_URL}choices/`)
      .then(response => {
        this.choices = response.data;
        localStorage.setItem('choices', JSON.stringify(response.data))
      })
    }
  })
