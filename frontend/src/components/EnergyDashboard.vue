<template>
  <div>
    <h2>Energy Consumption Dashboard</h2>
    <canvas id="energyChart"></canvas>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import Chart from 'chart.js/auto'

const chartRef = ref(null)

onMounted(async () => {
  const res = await fetch('http://localhost:8000/energy/')
  const data = await res.json()
  const labels = data.map(d => new Date(d.timestamp).toLocaleTimeString())
  const values = data.map(d => d.consumption_kwh)

  const ctx = document.getElementById('energyChart').getContext('2d')
  new Chart(ctx, {
    type: 'line',
    data: {
      labels,
      datasets: [{
        label: 'kWh',
        data: values,
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1
      }]
    }
  })
})
</script>

<style scoped>
#energyChart {
  max-width: 100%;
}
</style>
