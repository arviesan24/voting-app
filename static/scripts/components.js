
Vue.component('pie-chart', {
  extends: VueChartJs.Pie,
  mounted () {

    let randomHexColor = ['#'+(Math.random()*0xFFFFFF<<0).toString(16),];

    this.renderChart({
      labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
      datasets: [
        {
          label: 'Data One',
          backgroundColor: randomHexColor,
          data: [40, 39, 10, 40, 39, 80, 40]
        }
      ]
    }, {responsive: true, maintainAspectRatio: false})
  }
  
})
