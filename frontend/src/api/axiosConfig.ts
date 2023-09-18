import axios from 'axios';

const axiosInstance = axios.create();

axiosInstance.interceptors.request.use((config) => {
  // const accessToken = localStorage.getItem('accessToken');
  const accessToken = sessionStorage.getItem('accessToken');
  if (accessToken) {
    config.headers.Authorization = `Bearer ${accessToken}`;
  }
  return config;
});

export default axiosInstance;
