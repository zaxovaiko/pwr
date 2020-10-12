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
		return res.render('components/callback', {
			title: 'Error',
			text: 'You are already logged in',
		});
	}
	next();
};
