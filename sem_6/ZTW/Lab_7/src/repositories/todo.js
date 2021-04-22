const db = require("../helpers/database");
const { getOneById: getOneUserById } = require('./user');

function getAll() {
  return new Promise((res, rej) => {
    db.all("SELECT * FROM Todos", (err, todos) => (err ? rej() : res(todos)));
  });
}

function getOneById(id) {
  return new Promise((res, rej) => {
    db.get("SELECT * FROM Todos WHERE id = ?", id, (err, todo) =>
      err ? rej() : res(todo)
    );
  });
}

async function createOne({ title, user_id }) {
  const user = await getOneUserById(user_id);
  if (!user) {
    return null;
  }
  const todos = await getAll();
  const id = todos[todos.length - 1].id + 1;
  return await new Promise((res, rej) => {
    db.run(
      "INSERT INTO Todos VALUES (?, ?, ?, ?)",
      [id, title, false, user_id],
      (err) => (err ? rej() : res({ id, title, completed: false, user_id }))
    );
  });
}

function updateOneById(id, { title, completed }) {
  return getOneById(id).then(todo => {
    return new Promise((res, rej) => {
      db.run(
        "UPDATE Todos SET title = ?, completed = ?  WHERE id = ?",
        [title, completed, id],
        (err) => (err ? rej() : res({ id, title, completed, user_id: todo.user_id }))
      );
    });
  })
}

function deleteOneById(id) {
  return getOneById(id).then((todo) => {
    return new Promise((res, rej) => {
      db.run("DELETE FROM Todos WHERE id = ?", id, (err) =>
        err ? rej() : res(todo)
      );
    });
  });
}

module.exports = {
  getAll,
  getOneById,
  updateOneById,
  deleteOneById,
  createOne,
};
