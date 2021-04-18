<template>
  <div class="col mb-3">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title small">Pages: {{ book.pages }}</h5>
        <router-link
          :to="{ name: 'Book', params: { id: book.id } }"
          class="card-text text-dark"
        >
          {{ book.title.substr(0, 55) + "..." }}
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["book"],
};
</script>
