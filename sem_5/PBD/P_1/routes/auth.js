const express = require('express');
const validator = require('validator');
const bcrypt = require('bcrypt');

const router = express.Router();

const User = require('../models/User');
const authMiddleware = require('../middlewares/auth');

router.get('/login', [authMiddleware], (req, res) =>
	res.render('auth/login', {
		title: 'Login',
		user: req.session.user,
	})
);

router.get('/register', [authMiddleware], (req, res) =>
	res.render('auth/register', {
		title: 'Register',
		user: req.session.user,
	})
);

router.get('/logout', (req, res) => {
	req.session.destroy((err) => {
		if (err) {
			return res.render('404', {
				text: 'Bad session',
				desc: 'Try to relaod page and try again',
			});
		}
		res.redirect('/');
	});
});

/**
 * Log into user account.
 *
 * @methods POST
 * @route /login
 */
router.post(
	'/login',
	[
		authMiddleware,
		async (req, res, next) => {
			const user = await User.findOne({ email: req.body.email });
			if (user) {
				req.user = user;
				req.session.user = {
					_id: user._id,
					email: user.email,
					username: user.username,
				};
				return next();
			}

			res.render('404', { title: 'Error', text: 'User does not exist.' });
		},
	],
	async (req, res) => {
		try {
			if (bcrypt.compareSync(req.body.password, req.user.password)) {
				req.session.isLoggedIn = true;
				return res.redirect('/');
			}
		} catch (err) {}

		res.render('404', { text: 'Wrong password.' });
	}
);

/**
 * Register new user.
 *
 * @method POST
 * @route /register
 */
router.post(
	'/register',
	[
		authMiddleware,
		async (req, res, next) => {
			const user = await User.findOne({ email: req.body.email });
			if (user) {
				return res.render('404', { title: 'Error', text: 'User already exists.' });
			}
			next();
		},
	],
	async (req, res) => {
		// Validate passwords and other fields
		if (req.body.password === req.body.password_confirmation) {
			if (
				!validator.isEmpty(req.body.username) &&
				validator.isEmail(req.body.email) &&
				validator.isLength(req.body.password, {
					min: 6,
					max: 32,
				})
			) {
				// Store user in DB
				const hash = bcrypt.hashSync(req.body.password, 10);
				try {
					const user = await new User({
						username: validator.escape(req.body.username),
						email: req.body.email,
						password: hash,
					}).save();
					return res.render('components/callback', {
						text: `User ${user.username} was created`,
					});
				} catch (e) {}
			}
		}

		res.render('404', { title: 'Error', text: 'Something went wrong' });
	}
);

module.exports = router;
