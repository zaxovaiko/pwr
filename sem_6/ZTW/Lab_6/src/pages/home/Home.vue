<template>
  <div class="pt-5 pb-3">
    <h3 class="text-center display-4 mb-4 font-weight-bold">Find your book</h3>

    <input
      type="text"
      class="form-control form-control-lg"
      placeholder="Start typing..."
    />
  </div>

  <div class="row">
    <div class="col-12 col-md-8">
      <div class="row row-cols-1 row-cols-md-2 g-4">
        <BookItem
          v-bind:book="book"
          v-for="book of books"
          v-bind:key="book.id"
        />
      </div>
    </div>
    <div class="col-12 col-md-4">
      <router-link :to="{ name: 'AddBook' }" class="btn btn-outline-primary mb-3 w-100 rounded">
        Add book
      </router-link>
      <AuthorsList />
    </div>
  </div>
</template>

<script>
import faker from "faker";
import AuthorsList from "./AuthorsList";
import BookItem from "../../components/BookItem";

export default {
  data: function () {
    return {
      books: Array.from({ length: 10 }, () => ({
        id: faker.datatype.uuid(),
        title: faker.lorem.sentence(),
        author: faker.name.findName(),
        pages: faker.random.number({ min: 40, max: 1000 }),
      })),
    };
  },
  components: {
    AuthorsList,
    BookItem,
  },
};
</script>


<style scoped>
h5 {
  color: #aaa;
}
</style>