<template>
  <div class="py-5">
    <h3 class="text-center">Add new book</h3>

    <div class="mb-3">
      <label for="title" class="form-label">Title</label>
      <input type="email" class="form-control" id="title" placeholder="Title" />
    </div>

    <div class="mb-3">
      <label for="pages" class="form-label">Pages</label>
      <input
        type="number"
        class="form-control"
        id="pages"
        placeholder="Pages"
      />
    </div>

    <div class="mb-3">
      <label for="author_id" class="form-label">Author ID</label>
      <input
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
  </div>
</template>