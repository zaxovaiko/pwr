const dotenv = require("dotenv").config();
const sqlite3 = require("sqlite3").verbose();

module.exports = new sqlite3.Database(process.env.DB_NAME + '.sqlite');