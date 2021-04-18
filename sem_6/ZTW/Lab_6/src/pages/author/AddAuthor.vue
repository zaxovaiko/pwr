<template>
  <div class="py-5 w-50 mx-auto my-5">
    <h3 class="text-center">Add new author</h3>

    <div v-if="error && error.message" class="alert alert-danger" role="alert">
      {{ error.message }}
    </div>

    <div v-if="success" class="alert alert-success mt-3" role="alert">
      New author was added
    </div>

    <form @submit="submitForm" method="post">
      <div class="mb-3">
        <label for="title" class="form-label">First name</label>
        <input
          type="text"
          v-model="firstName"
          class="form-control"
          id="firstName"
          placeholder="First name"
        />
      </div>

      <div class="mb-3">
        <label for="title" class="form-label">Second name</label>
        <input
          type="text"
          v-model="lastName"
          class="form-control"
          id="secondName"
          placeholder="Second name"
        />
      </div>

      <div class="mb-3">
        <label for="pages" class="form-label">Age</label>
        <input
          v-model="age"
          type="number"
          class="form-control"
          id="age"
          placeholder="Age"
        />
      </div>

      <div class="text-right">
        <router-link :to="{ name: 'Home' }" class="btn btn-outline-danger mr-2">
          Go back
        </router-link>
        <button class="btn btn-success">Add author</button>
      </div>
    </form>
  </div>
</template>


<script>
export default {
  data() {
    return {
      error: {},
      firstName: "",
      lastName: "",
      success: false,
      age: 0,
    };
  },
  methods: {
    submitForm(e) {
      e.preventDefault();

      fetch("http://localhost:8080/authors", {
        method: "POST",
        body: new URLSearchParams({
          firstName: this.firstName,
          lastName: this.lastName,
          age: this.age,
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
