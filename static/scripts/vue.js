Vue.options.delimiters = ['[[', ']]'];

var vm = new Vue({
    el: '.app',
    data: {},
    mounted() {
      axios.get(`${API_ROOT_URL}choices/`);
    }
  })
