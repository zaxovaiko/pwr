const {
  getAll,
  getOneById,
  createOne,
  deleteOneById,
  updateOneById,
} = require("../repositories/user");
const { getAll: getAllTodos } = require("../repositories/todo");

module.exports = {
  Query: {
    users: () => getAll(),
    user: (_, { id }) => getOneById(id),
  },
  Mutation: {
    addUser: (_, args) => createOne(args),
    editUser: (_, args) => updateOneById(args.id, args),
    deleteUser: (_, { id }) => deleteOneById(id),
  },
  User: {
    todos: (parent) =>
      getAllTodos().then((res) => res.filter((e) => e.user_id === parent.id)),
  },
};
