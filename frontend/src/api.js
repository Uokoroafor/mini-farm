import axios from 'axios';

// Create an instance of axios with the base URL
const api = axios.create({
  baseURL: "http://localhost:3001",
  withCredentials: true,
});

// Add auth token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Export the Axios instance
export default api;