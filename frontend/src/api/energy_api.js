import axios from 'axios';

const api = axios.create({
  baseURL: process.env.VUE_APP_API_BASE_URL || 'http://localhost:8000',
  timeout: 10000,
});

export const getEnergyData = () => api.get('/energy/consumption');
export const getPrediction = () => api.get('/energy/prediction');
export const getReport = () => api.get('/energy/report');
