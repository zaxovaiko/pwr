<template>
  <div class="row py-5 mt-5">
    <p v-if="!book">Book does not exists</p>
    <p v-if="error && error.message">Something went wrong</p>
    <div v-if="book" class="col-8 offset-2">
      <p>Book</p>
      <h3>
        "{{ book.title }}"
        <router-link
          class="float-right text-primary"
          :to="{ name: 'EditBook', params: { id: book.id } }"
        >
          <span>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="26"
              height="26"
              fill="currentColor"
              class="bi bi-pencil-square"
              viewBox="0 0 16 16"
            >
              <path
                d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"
              />
              <path
                fill-rule="evenodd"
                d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"
              /></svg
          ></span>
        </router-link>
      </h3>
      <p>pages: {{ book.pages }}</p>
      <hr />
      <p v-if="!author">Author does not exists</p>
      <div v-if="author">
        <p>Author</p>
        <h3>
          {{ author.firstName }} {{ author.lastName }}, {{ author.age }} lat
        </h3>
      </div>
      <router-link :to="{ name: 'Home' }" class="btn btn-danger">
        Back
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      book: null,
      author: null,
      loading: false,
      error: {},
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      fetch("http://localhost:8080/books/" + this.$route.params.id)
        .then((res) => res.json())
        .then((res) => {
          this.book = res;
          fetch("http://localhost:8080/authors/" + res.author)
            .then((res) => res.json())
            .then((author) => {
              this.author = author;
            });
        })
        .catch((err) => {
          this.error = err;
        });
    },
  },
};
</script>
