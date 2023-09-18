import axios from 'axios';

const http = axios.create({
    baseURL: 'http://localhost:8000',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    },
});

http.interceptors.request.use(
    config => {
        // const token = localStorage.getItem('accessToken');
        const token = sessionStorage.getItem('accessToken');
        if (token) {
            config.headers.Authorization = `Token ${token}`;
        }
        return config;
    }, error => {
        console.error('Error intercepting request axios:', error);
        return Promise.reject(error);
    }
);

export default http;
