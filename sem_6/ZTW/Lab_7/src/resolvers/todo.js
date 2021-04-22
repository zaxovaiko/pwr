const { getAll: getAllUsers } = require("../repositories/user");
const {
  getAll,
  getOneById,
  createOne,
  updateOneById,
  deleteOneById,
} = require("../repositories/todo");

module.exports = {
  Query: {
    todos: () => getAll(),
    todo: (_, { id }) => getOneById(id),
  },
  Mutation: {
    addTodo: (_, args) => createOne(args),
    editTodo: (_, args) => updateOneById(args.id, args),
    deleteTodo: (_, args) => deleteOneById(args.id),
  },
  Todo: {
    user: (parent) =>
      getAllUsers().then((res) => res.find((e) => e.id === parent.user_id)),
  },
};
