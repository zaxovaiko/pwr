const mongoose = require('mongoose');

module.exports = mongoose.model(
	'Inventory',
	new mongoose.Schema(
		{
			product_id: {
				type: mongoose.SchemaTypes.ObjectID,
				required: true,
			},
			count: {
				type: Number,
				default: 0,
			},
		},
		{
			timestamps: {
				createdAt: 'created_at',
				updatedAt: 'updated_at',
			},
		}
	)
);
