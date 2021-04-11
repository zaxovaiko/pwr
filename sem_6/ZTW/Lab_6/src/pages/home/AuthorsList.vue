<template>
  <h4>Authors</h4>

  <div class="list-group">
    <a href="#" class="list-group-item list-group-item-action active"
      ><svg
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
      Add author</a
    >
    <a
      v-bind:key="author.id"
      v-for="author of authors"
      href="#"
      class="list-group-item list-group-item-action"
    >
      {{ author.firstName }} {{ author.lastName }}, age {{ author.age }}
    </a>
  </div>
</template>

<script>
import faker from "faker";

const authors = Array.from({ length: 6 }, () => ({
  id: faker.datatype.uuid(),
  firstName: faker.name.firstName(),
  lastName: faker.name.lastName(),
  age: faker.random.number({ min: 20, max: 80 }),
}));

export default {
  data: function () {
    return {
      authors,
    };
  },
};
</script>
