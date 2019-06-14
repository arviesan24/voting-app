Vue.options.delimiters = ['[[', ']]'];
Vue.component('poll-delete-modal', {
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
              Are you sure you want to delete this poll?
            </slot>
          </div>

          <div class="modal-footer">
            <slot name="footer">
            <button class="btn btn-outline-info" @click="$emit('close')">
              Cancel
            </button>
              <button class="btn btn-danger" @click="deletePoll(); $emit('close')">
                Yes
              </button>
            </slot>
          </div>
        </div>
      </div>
    </div>
  </transition>
  `,
  data() {
    return {
    }
  },
  methods: {
    deletePoll() {
      axios({
        method: "delete",
        url: `${API_ROOT_URL}polls/${pollId}/`,
        headers: {
          'Authorization': auth_user_token
        }
      }).then(response => {
        window.location.replace(myPollUrl);
      });
    }
  }
})
