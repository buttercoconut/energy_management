<template>
  <div class="dashboard">
    <h2>Real‑Time Energy Consumption</h2>
    <div v-if="loading" class="loading">Loading...</div>
    <div v-else>
      <table class="table">
        <thead>
          <tr>
            <th>Timestamp</th>
            <th>Consumption (kWh)</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, idx) in data" :key="idx">
            <td>{{ item.timestamp }}</td>
            <td>{{ item.consumption.toFixed(2) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { getEnergyData } from '../api/energy_api.js';

const data = ref([]);
const loading = ref(true);
let intervalId;

const fetchData = async () => {
  try {
    const res = await getEnergyData();
    data.value = res.data;
    loading.value = false;
  } catch (e) {
    console.error('Failed to fetch energy data', e);
  }
};

onMounted(() => {
  fetchData();
  intervalId = setInterval(fetchData, 5000); // poll every 5 seconds
});

onUnmounted(() => {
  clearInterval(intervalId);
});
</script>

<style scoped>
.dashboard {
  padding: 1rem;
}
.table {
  width: 100%;
  border-collapse: collapse;
}
.table th,
.table td {
  border: 1px solid #ddd;
  padding: 0.5rem;
}
.loading {
  font-style: italic;
}
</style>
