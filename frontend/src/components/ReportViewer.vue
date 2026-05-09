<template>
  <div class="report-viewer">
    <h2>Energy Consumption Report</h2>
    <div v-if="loading" class="loading">Loading report...</div>
    <div v-else>
      <table class="table">
        <thead>
          <tr>
            <th>Date</th>
            <th>Total Consumption (kWh)</th>
            <th>Peak Consumption (kWh)</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(row, idx) in report" :key="idx">
            <td>{{ row.date }}</td>
            <td>{{ row.total.toFixed(2) }}</td>
            <td>{{ row.peak.toFixed(2) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { getReport } from '../api/energy_api.js';

const report = ref([]);
const loading = ref(true);

const fetchReport = async () => {
  try {
    const res = await getReport();
    report.value = res.data;
  } catch (e) {
    console.error('Failed to fetch report', e);
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  fetchReport();
});
</script>

<style scoped>
.report-viewer {
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
