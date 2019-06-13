Vue.component('choice-add-form', {
  template: `
  <div class="input-group mb-3">
    <input type="text" v-model="newChoice" class="form-control" placeholder="Add Choice">
    <div class="input-group-append">
      <button v-bind:disabled="newChoice==null||newChoice==''||!newChoice.trim()" class="btn btn-primary" v-on:click="saveChoice()">Save</button>  
     </div>
  </div>
  `,
  data() {
    return {
      newChoice: null
    }
  },
  methods: {
    saveChoice() {
      axios({
        method: 'post',
        url: `${API_ROOT_URL}choices/`,
        headers: {
          'Authorization': auth_user_token
        },
        data: {
          poll: `${API_ROOT_URL}polls/${pollId}/`,
          name: this.newChoice
        }
      })
      .then(() => {
        this.$parent.loadChoices();
      });
    }
  }
});
