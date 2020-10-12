const faker = require('faker');

const Category = require('../models/Category');

/**
 * Store <count> categories into DB.
 *
 * @param count
 * @returns {Promise<number>}
 */
module.exports = function (count) {
	return new Promise((res, rej) => {
		(async () => {
			// Clear collection before writing
			await Category.deleteMany();

			let done = 0;
			for (let i = 0; i < count; i++) {
				const cat = await new Category({
					name: faker.lorem.word(),
					description: faker.lorem.sentence(),
				}).save();
				done += Number(!!cat);
			}
			done === count ? res(done) : rej(done);
		})();
	});
};
