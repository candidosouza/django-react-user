import axios from 'axios';

const baseApiUrl = process.env.REACT_APP_API_URL;

const http = axios.create({
    // change amazon ec2 ip address here
    baseURL: baseApiUrl,
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
