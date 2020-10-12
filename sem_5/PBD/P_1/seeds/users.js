const faker = require('faker');
const bcrypt = require('bcrypt');

const User = require('../models/User');

/**
 * Store <count> users into DB.
 *
 * @param count
 * @returns {Promise<>}
 */
module.exports = function seedUsers(count) {
	return new Promise((res, rej) => {
		(async () => {
			// Clear collection before writing
			await User.deleteMany();

			let done = 0;
			for (let i = 0; i < count; i++) {
				const user = await new User({
					username: faker.internet.userName(),
					email: faker.internet.email(),
					password: bcrypt.hashSync('password', 10),
				}).save();
				done += Number(!!user);
			}
			done === count ? res(done) : rej(done);
		})();
	});
};
