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
              <small v-if="pollTitleError" class="text-danger">{{pollTitleError}}</small>
              <textarea v-on:input="pollDescriptionValidation" v-model="pollDescription" class="form-control my-2" placeholder="Add Description" rows="3"></textarea>
              <small v-if="pollDescriptionError" class="text-danger">{{pollDescriptionError}}</small>
              <textarea v-on:input="pollChoicesValidation" v-model="pollChoices" class="form-control my-2" placeholder="Add Choices (seperated by line)" rows="5"></textarea>
              <small v-if="pollChoicesError" class="text-danger">{{pollChoicesError}}</small>
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
      pollChoices: '',
      pollTitleError: 'Title is required.',
      pollDescriptionError: 'Description is required.',
      pollChoicesError: 'Choices are required.'
    }
  },
  computed: {
    choicesArray: function() {
      return this.pollChoices.split('\n');
    },
    inputsValid() {
      if (this.pollTitle==null||this.pollTitle==''||!this.pollTitle.trim()) {
        return false;
      } else if (this.pollDescription==null||this.pollDescription==''||!this.pollDescription.trim()) {
        return false;
      } else if (this.pollChoices==null||this.pollChoices==''||!this.pollChoices.trim()) {
        return false;
      } else {
        return true;
      }
    }
  },
  methods: {
    pollTitleValidation() {
      if (this.pollTitle==null||this.pollTitle==''||!this.pollTitle.trim()) {
        this.pollTitleError = 'Title is required.';
        return false;
      } else {
        this.pollTitleError = null
        return true
      }
    },
    pollDescriptionValidation() {
      if (this.pollDescription==null||this.pollDescription==''||!this.pollDescription.trim()) {
        this.pollDescriptionError = 'Description is required.';
        return false;
      } else {
        this.pollDescriptionError = null
        return true;
      }
    },
    pollChoicesValidation() {
      if (this.pollChoices==null||this.pollChoices==''||!this.pollChoices.trim()) {
        this.pollChoicesError = 'Choices are required.';
        return false;
      } else {
        this.pollChoicesError = null
        return true;
      }
    }
  }
})
