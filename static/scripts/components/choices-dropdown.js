Vue.component('choices-dropdown', {
  props: {
    options: {
      type: Array,
      required: true
    }
  },
  template: `
  <div>
    <select v-on:change="getSelected">
      <option v-for="option in options" v-bind:value="option.value">{{ option.name }}</option>
    </select>
  </div>
  `,
  methods: {
    getSelected(e) {
      // Get the value from here: v-on:change="getSelected"
      // it will auto generate an event variable (e).
      // emit `e.target.value` under the name of `emit-selected`
      // which will become a custom event in parent template.
      this.$emit('emit-selected',  e.target.value);
    }
  }
})
