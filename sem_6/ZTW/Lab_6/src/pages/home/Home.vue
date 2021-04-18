<template>
  <div class="pt-5 pb-3">
    <h3 class="text-center display-4 mb-4 font-weight-bold">Find your book</h3>

    <input
      type="text"
      @input="findQuery"
      class="form-control form-control-lg"
      placeholder="Start typing..."
    />

    <div
      class="mt-3 alert alert-warning alert-dismissible fade show"
      role="alert"
      v-if="message"
    >
      {{ message }}
      <button
        type="button"
        class="btn-close"
        data-bs-dismiss="alert"
        aria-label="Close"
      ></button>
    </div>
  </div>

  <div class="row">
    <div class="col-12 col-md-8">
      <p v-if="filteredBooks.length === 0">There is not any book yet</p>
      <div
        v-if="filteredBooks.length > 0"
        class="row row-cols-1 row-cols-md-2 g-4"
      >
        <BookItem
          v-bind:book="book"
          v-for="book of filteredBooks"
          v-bind:key="book.id"
        />
      </div>
    </div>
    <div class="col-12 col-md-4">
      <router-link
        :to="{ name: 'AddBook' }"
        class="btn btn-outline-primary mb-3 w-100 rounded"
      >
        Add book
      </router-link>
      <AuthorsList />
    </div>
  </div>
</template>

<script>
import AuthorsList from "./AuthorsList";
import BookItem from "../../components/BookItem";

export default {
  data: function () {
    return {
      filteredBooks: [],
      loading: false,
      books: [],
      error: null,
    };
  },
  mounted() {
    this.fetchBooks();
  },
  components: {
    AuthorsList,
    BookItem,
  },
  methods: {
    fetchBooks() {
      this.loading = true;
      fetch("http://localhost:8080/books")
        .then((res) => res.json())
        .then((res) => {
          this.books = res;
          this.filteredBooks = res;
        })
        .catch((err) => {
          console.log(err);
          this.error = err;
        });
    },
    findQuery(e) {
      this.filteredBooks = this.books.filter((book) =>
        book.title.includes(e.target.value)
      );
    },
  },
};
</script>


<style scoped>
h5 {
  color: #aaa;
}
</style>