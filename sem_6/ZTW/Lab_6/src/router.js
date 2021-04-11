import { createWebHistory, createRouter } from "vue-router";

import Home from "./pages/home/Home";
import AddBook from "./pages/AddBook";

const routes = [
  { path: "/", name: 'Home', component: Home },
  { path: "/book/add", name: 'AddBook', component: AddBook },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
