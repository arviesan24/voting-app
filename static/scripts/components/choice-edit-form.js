Vue.component('modal', {
  props: {
    choiceToUse: Object
  },
  data() {
    return {
      choice: {}
    }
  },
  mounted() {
    this.choice = this.choiceToUse;
  },
  methods: {
    editChoice() {
      axios({
        method: 'patch',
        url: `${API_ROOT_URL}choices/${this.choice.id}/`,
        headers: {
          'Authorization': auth_user_token
        },
        data: {
          name: this.choice.name
        }
      })
      .then(response => {
        console.log(response);
      });
    } 
  },
  template: `
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">

          <div class="modal-header">
            <slot name="header">
            </slot>
          </div>

          <div class="modal-body">
            <slot name="body">
              <input v-model="choice.name" type="text" />
            </slot>
          </div>

          <div class="modal-footer">
            <slot name="footer">
              <button class="btn btn-outline-primary btn-small" @click="$emit('close');">Cancel</button>
              <button class="modal-default-button btn btn-primary btn-small" @click="editChoice(); $emit('close');">Save</button>
              </slot>
          </div>
        </div>
      </div>
    </div>
  </transition>
  `
})