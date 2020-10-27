/**
 * Checks if user is already logged in.
 *
 * @param req
 * @param res
 * @param next
 * @returns {void|undefined}
 */
module.exports = function (req, res, next) {
	if (req.session.isLoggedIn) {
		return res.render('404', {
			title: 'Error',
			text: 'Permission denied',
			desc: 'You are already logged in',
			user: false,
		});
	}
	next();
};
