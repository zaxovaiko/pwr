<template>
  <h4>Authors</h4>

  <div class="list-group">
    <router-link
      :to="{ name: 'AddAuthor' }"
      class="list-group-item list-group-item-action active"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="16"
        height="16"
        fill="currentColor"
        class="bi bi-plus-square mr-2"
        viewBox="0 0 16 16"
      >
        <path
          d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"
        />
        <path
          d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"
        />
      </svg>
      Add author
    </router-link>
    <a
      v-bind:key="author.id"
      v-for="author of authors"
      href="#"
      class="list-group-item list-group-item-action"
    >
      {{ author.firstName }} {{ author.lastName }}, age {{ author.age }}
      <span class="float-right" @click="deleteAuthor(author.id)">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          fill="currentColor"
          class="bi bi-trash"
          viewBox="0 0 16 16"
        >
          <path
            d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"
          />
          <path
            fill-rule="evenodd"
            d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"
          />
        </svg>
      </span>
    </a>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      authors: null,
    };
  },
  created() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      fetch("http://localhost:8080/authors")
        .then((res) => res.json())
        .then((res) => (this.authors = res))
        .catch((err) => console.log(err));
    },
    deleteAuthor(id) {
      fetch("http://localhost:8080/authors/" + id, {
        method: "DELETE",
      })
        .then((res) => res.json())
        .then(() => {
          this.authors = this.authors.filter((e) => e.id !== id);
          this.message = "Author was deleted";
        })
        .catch((err) => console.log(err));
    },
  },
};
</script>
