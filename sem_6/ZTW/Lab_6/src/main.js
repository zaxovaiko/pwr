import 'bootstrap/dist/css/bootstrap.min.css';
import { createApp } from 'vue';
import router from './router';
import App from './App';

createApp(App).use(router).mount('#app');
