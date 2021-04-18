<template>
  <div class="py-5 w-50 mx-auto my-5">
    <h3 class="text-center">Add new book</h3>

    <div v-if="error && error.message" class="alert alert-danger" role="alert">
      {{ error.message }}
    </div>

    <div v-if="success" class="alert alert-success mt-3" role="alert">
      New book was added
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
        <router-link :to="{ name: 'Home' }" class="btn btn-outline-danger mr-2">
          Go back
        </router-link>
        <button class="btn btn-success">Add book</button>
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
  methods: {
    submitForm(e) {
      e.preventDefault();

      fetch("http://localhost:8080/books", {
        method: "POST",
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
