<template>
  <h3>{{ title }}</h3>
  <input type="text" v-bind:value="currentInput" v-on:input="handleInput" />
  <button v-on:click="addToList">Add to list</button>
  <p>{{ currentInput }}</p>
  <ul>
    <li v-bind:key="todo" v-for="todo in todos">{{ todo }}</li>
  </ul>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      title: "To-do list",
      currentInput: "",
      todos: []
    }
  },
  methods: {
    handleInput(e) {
      this.currentInput = e.target.value;
    },
    addToList() {
      this.todos.push(this.currentInput);
    }
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
