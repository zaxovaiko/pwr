const express = require('express');
const router = express.Router();

router.get('*', (req, res) => {
	res.render('404', { title: 'Error', text: 'Not found' });
});

module.exports = router;
