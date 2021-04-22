const db = require("../helpers/database");

function getAll() {
  return new Promise((res, rej) => {
    db.all("SELECT * FROM Users", (err, users) => (err ? rej() : res(users)));
  });
}

function getOneById(id) {
  return new Promise((res, rej) => {
    db.get("SELECT * FROM Users WHERE id = ?", id, (err, user) =>
      err ? rej() : res(user)
    );
  });
}

function createOne({ name, login, email }) {
  return getAll().then((users) => {
    const id = users[users.length - 1].id + 1;
    return new Promise((res, rej) => {
      db.run(
        "INSERT INTO Users VALUES (?, ?, ?, ?)",
        [id, name, email, login],
        (err) => (err ? rej() : res({ id, name, email, login }))
      );
    });
  });
}

function updateOneById(id, { name, email, login }) {
  return new Promise((res, rej) => {
    db.run(
      "UPDATE Users SET name = ?, email = ?, login = ? WHERE id = ?",
      [name, email, login, id],
      (err) => (err ? rej() : res({ name, email, login, id }))
    );
  });
}

function deleteOneById(id) {
  return getOneById(id).then((user) => {
    return new Promise((res, rej) => {
      db.run("DELETE FROM Users WHERE id = ?", id, (err) =>
        err ? rej() : res(user)
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
