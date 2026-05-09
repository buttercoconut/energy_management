import axios from 'axios'

export default {
  name: 'EnergyAPI',
  methods: {
    async getEnergyData() {
      const response = await axios.get('http://localhost:8000/energy/')
      return response.data
    }
  }
}
