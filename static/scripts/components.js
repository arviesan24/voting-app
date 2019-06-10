
Vue.component('pie-chart', {
  extends: VueChartJs.Pie,
  props: {
    propChoices: Array
  },
  mounted () {
    const choices = this.propChoices;
    let randomHexColor = [];
    let chartLabels = [];
    let chartData = [];
    choices.forEach(choice => {
      randomHexColor.push('#'+(Math.random()*0xFFFFFF<<0).toString(16));
      chartLabels.push(choice.name);
      chartData.push(choice.total_votes);
    });

    this.renderChart({
      labels: chartLabels,
      datasets: [
        {
          label: 'Poll Result',
          backgroundColor: randomHexColor,
          data: chartData
        }
      ]
    }, {responsive: true, maintainAspectRatio: false})
  }
  
})
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
