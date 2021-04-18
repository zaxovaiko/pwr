<template>
  <div class="py-5 w-50 mx-auto my-5">
    <h3 class="text-center">Add new book</h3>

    <div v-if="error && error.message" class="alert alert-danger" role="alert">
      {{ error.message }}
    </div>

    <div v-if="success" class="alert alert-success mt-3" role="alert">
      Book was updated
    </div>

    <form @submit="submitForm" method="post">
      <div class="mb-3">
        <label for="title" class="form-label">Title</label>
        <input
          v-model="title"
          type="text"
          class="form-control"
          id="title"
          placeholder="Title"
        />
      </div>

      <div class="mb-3">
        <label for="pages" class="form-label">Pages</label>
        <input
          v-model.number="pages"
          type="number"
          class="form-control"
          id="pages"
          placeholder="Pages"
        />
      </div>

      <div class="mb-3">
        <label for="author_id" class="form-label">Author ID</label>
        <input
          v-model="author_id"
          type="text"
          class="form-control"
          id="author_id"
          placeholder="Author ID"
        />
      </div>

      <div class="text-right">
        <router-link
          :to="{ name: 'Book', params: { id: this.$route.params.id } }"
          class="btn btn-outline-danger mr-2"
        >
          Go back
        </router-link>
        <button class="btn btn-success">Update book</button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      error: {},
      title: "",
      success: false,
      pages: 0,
      author_id: "",
    };
  },
  created() {
    this.fetchBook();
  },
  methods: {
    fetchBook() {
      fetch("http://localhost:8080/books/" + this.$route.params.id)
        .then((res) => res.json())
        .then((res) => {
          this.title = res.title;
          this.author_id = res.author;
          this.pages = res.pages;
        })
        .catch((err) => console.log(err));
    },
    submitForm(e) {
      e.preventDefault();

      fetch("http://localhost:8080/books/" + this.$route.params.id, {
        method: "PUT",
        body: new URLSearchParams({
          title: this.title,
          pages: this.pages,
          authorId: this.author_id,
        }),
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      })
        .then((res) => res.json())
        .then(() => {
          this.success = true;
        })
        .catch((err) => {
          this.error = err;
          console.log(err);
        });
    },
  },
};
</script>
