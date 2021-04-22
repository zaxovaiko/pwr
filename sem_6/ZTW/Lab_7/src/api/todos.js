const axios = require("axios");

module.exports = async function getRestTodosList() {
  const todos = await axios.get("https://jsonplaceholder.typicode.com/todos");
  return todos.data.map((e) => ({
    id: e.id,
    title: e.title,
    completed: e.completed,
    user_id: e.userId,
  }));
};
