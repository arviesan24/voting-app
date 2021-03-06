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
    },
    saveNewPoll() {
      axios({
        method: "post",
        url: `${API_ROOT_URL}polls/`,
        headers: {
          'Authorization': auth_user_token
        },
        data: {
          owner: `${API_ROOT_URL}users/${userId}/`,
          title: this.newPoll.title,
          description: this.newPoll.description
        }
      })
      .then(response => {
        let newPollUrl = response.data.url;
        let choices = this.newPoll.choices;

        return choices.forEach(choice => {
          axios({
            method: "post",
            url: `${API_ROOT_URL}choices/`,
            headers: {
              'Authorization': auth_user_token
            },
            data: {
              poll: newPollUrl,
              name: choice
            }
          });
        });
      }).then(() => location.reload(true))
      .catch((error) => {
        console.log(error);
      });
    }
  },
})
