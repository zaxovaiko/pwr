const faker = require('faker');

const Category = require('../models/Category');
const Product = require('../models/Product');

/**
 * Store <count> products into DB.
 *
 * @param count
 * @returns {Promise<>}
 */
module.exports = function seedProducts(count) {
	return new Promise((res, rej) => {
		(async () => {
			// Clear collection before writing
			await Product.deleteMany();

			const categories = await Category.find();

			let done = 0;
			for (let i = 0; i < count; i++) {
				const product = await new Product({
					title: faker.commerce.productName(),
					description: faker.commerce.productDescription(),
					images: [faker.image.lorempicsum.image(500, 500, true)],
					price: faker.random.float(),
					category: categories[Math.ceil(Math.random() * categories.length) - 1]._id,
				}).save();
				done += Number(!!product);
			}
			done === count ? res(done) : rej(done);
		})();
	});
};
