const express = require('express');
const router = express.Router();

router.get('/login', (req, res) => {
	res.render('index', { title: 'Login', message: 'Users login' });
});

router.post('/login', (req, res) => {
	// login post
});

router.get('/register', (req, res) => {
	res.send('Register page');
});

router.post('/register', (req, res) => {
	// register post
});

module.exports = router;
