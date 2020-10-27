require('dotenv').config();
const express = require('express');
const session = require('express-session');
const mongoose = require('mongoose');
const path = require('path');

const indexRouter = require('./routes/index');
const authRouter = require('./routes/auth');

const app = express();

// Database connection
mongoose
	.connect(process.env.MONGODB_URI, {
		useNewUrlParser: true,
		useUnifiedTopology: true,
	})
	.then((_) => console.log('Connected to MongoDB'))
	.catch((error) => console.log(error));

// Other Express stuff
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

app.use(
	session({
		secret: process.env.SESSION_SECRET,
		secure: false,
		maxAge: 360000,
		cookie: { secure: false },
		resave: false,
		saveUninitialized: false,
	})
);
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);
app.use('/', authRouter);
app.use((req, res) => {
	res.render('404', { title: 'Error', text: 'Not found', user: req.session.user });
});

module.exports = app;
