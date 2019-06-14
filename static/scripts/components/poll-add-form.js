Vue.component('poll-add-form', {
  template: `
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">

          <div class="modal-header">
            <slot name="header">
              default header
            </slot>
          </div>

          <div class="modal-body">
            <slot name="body">
              <input type="text" v-on:input="pollTitleValidation" v-model="pollTitle" class="form-control my-2" placeholder="Add Title">
              <small class="text-danger">[[pollTitleError]]</small>
              <textarea v-on:input="pollDescriptionValidation" v-model="pollDescription" class="form-control my-2" placeholder="Add Description" rows="3"></textarea>
              <small class="text-danger">[[pollDescriptionError]]</small>
              <textarea v-on:input="pollChoicesValidation" v-model="pollChoices" class="form-control my-2" placeholder="Add Choices (seperated by line)" rows="5"></textarea>
              <small class="text-danger">[[pollChoicesError]]</small>
            </slot>
          </div>

          <div class="modal-footer">
            <slot name="footer">
              <button class="btn btn-outline-info" @click="$emit('close')">
                Cancel
              </button>
              <button class="btn btn-info" @click="$emit('close')">
                Save
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
      pollTitle: '',
      pollDescription: '',
      pollChoices: ''
    }
  },
  computed: {
    choicesArray: function() {
      return this.pollChoices.split('\n');
    }
  }
})
