<template>
  <div>Author: {{ this.$route.params.id }}</div>
</template>

<script>
export default {
  data() {
    return {
      author: {
        firstName: "",
        secondName: "",
        age: 0,
      },
    };
  },
};
</script>
