import axios from 'axios';

let instance = axios.create({
    baseURL: "http://localhost:8080/"
});

instance.interceptors.request.use(config => {
    const token = localStorage.getItem('access_token');
    if (token) {
        config.headers['Authorization'] = 'Bearer ' + token;
    }
    return config;
},
error => {
    Promise.reject(error)
});

export default instance;