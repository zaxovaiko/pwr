require('dotenv').config();
const mongoose = require('mongoose');

const userSeeder = require('./users');
const categorySeeder = require('./categories');
const productSeeder = require('./products');

(async () => {
	try {
		// Database connection
		const conn = await mongoose.connect(process.env.MONGODB_URI, {
			useNewUrlParser: true,
			useUnifiedTopology: true,
		});
		if (conn) {
			console.log('Connected to MongoDB.');
		}

		console.log((await userSeeder(10)) + ' users were written to db.');
		console.log((await categorySeeder(10)) + ' categories were written to db.');
		console.log((await productSeeder(10)) + ' products were written to db.');

		conn.connection.close();
	} catch (e) {
		console.log('Something went wrong. Try again.');
		process.exit(1);
	}
})();
