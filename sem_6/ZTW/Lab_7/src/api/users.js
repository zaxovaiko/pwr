const axios = require("axios");

module.exports = async function getRestUsersList() {
  const users = await axios.get("https://jsonplaceholder.typicode.com/users");
  return users.data.map((e) => ({
    id: e.id,
    name: e.name,
    email: e.email,
    login: e.username,
  }));
};
