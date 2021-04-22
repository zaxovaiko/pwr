const { GraphQLServer } = require("graphql-yoga");

const userResolver = require("./resolvers/user");
const todoResolver = require("./resolvers/todo");

const server = new GraphQLServer({
  typeDefs: "./src/schema.graphql",
  resolvers: {
    ...userResolver,
    ...todoResolver,
    Query: {
      ...userResolver.Query,
      ...todoResolver.Query,
    },
    Mutation: {
      ...userResolver.Mutation,
      ...todoResolver.Mutation,
    },
  },
});

server.start(() => console.log("Server is running on port 4000"));
