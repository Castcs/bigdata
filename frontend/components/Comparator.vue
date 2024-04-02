<template>
  <div class="team-summary">
    <h1>Cost of Living Comparison</h1>
    <div class="chart-container">
      <Bar :data="data" :options="options" />
    </div>
  </div>
</template>

<script>
import { Bar } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
} from 'chart.js'
ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend)

export default {
  components: {
    Bar
  },
  setup() {
    const data = {
      labels: ['Raleigh', 'Greenville', 'Charlotte', 'Nashville', 'New York', 'San Francisco'],
      datasets: [
        {
          label: 'Software Developer Salary (Thousands of Dollars per Year)',
          backgroundColor: '#0000ff',
          data: [145.0, 96.0, 148.0, 177.0, 211.5, 234.5]
        }
      ]
    };
    const options = {
      responsive: true,
      maintainAspectRatio: false,
    };

    return {
      data,
      options,
    };
  },
};
</script>
<style>
.chart-container {
  position: relative;
  margin: auto;
  height: 400px;
  width: 800px;
}
h1{
  color: blue;
}
</style>