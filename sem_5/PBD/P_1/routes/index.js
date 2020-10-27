const express = require('express');
const router = express.Router();

const Product = require('../models/Product');

/**
 * Root path.
 *
 * @method GET
 * @route /
 */
router.get('/', async (req, res) => {
	res.render('home', {
		title: 'Main page',
		user: req.session.user,
		products: await Product.find().limit(4),
	});
});

module.exports = router;
