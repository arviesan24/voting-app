Vue.component('choices-list', {
  props: {
    choices: Array,
  },
  template: `
  <div>
    <table class="table table-striped">
      <tbody>
        <tr v-for="choice in choices">
          <th scope="row">{{choice.name}}</th>
          <td><button v-on:click="choiceDataToModal(choice)" class="btn btn-success btn-sm mr-2"><i class="fa fa-edit"></i></button><button v-on:click="deleteChoice(choice.id)" class="btn btn-danger btn-sm"><i class="fa fa-trash"></i></button></td>
        </tr>
      </tbody>
    </table>
  </div>
  `,
  methods: {
    deleteChoice(choiceId) {
      axios.delete(`${API_ROOT_URL}choices/${choiceId}/`, {headers: {'Authorization': auth_user_token}})
      .then(() => {
        this.$parent.loadChoices();
      });
    },
    choiceDataToModal(choice) {
      this.$emit('emit-selected-choice',  choice);
    }
  },
});
