import { createWebHistory, createRouter } from "vue-router";

import Home from "./pages/home/Home";
import AddBook from "./pages/book/AddBook";
import EditBook from "./pages/book/EditBook";
import Book from "./pages/book/Book";
import AddAuthor from "./pages/author/AddAuthor";
import Author from "./pages/author/Author";

const routes = [
  { path: "/", name: 'Home', component: Home },
  { path: "/books/add", name: 'AddBook', component: AddBook },
  { path: "/books/edit/:id", name: 'EditBook', component: EditBook },
  { path: "/books/:id", name: 'Book', component: Book },
  { path: "/authors/add", name: 'AddAuthor', component: AddAuthor },
  { path: "/authors/:id", name: 'Author', component: Author },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
