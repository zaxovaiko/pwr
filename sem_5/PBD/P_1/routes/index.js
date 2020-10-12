const express = require('express');
const router = express.Router();

/**
 * Root path.
 *
 * @method GET
 * @route /
 */
router.get('/', (req, res) => {
	res.render('index', {
		title: 'Main page',
		name: req.session.user ? req.session.user.username : 'guest',
	});
});

module.exports = router;
