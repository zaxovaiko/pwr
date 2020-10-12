const mongoose = require('mongoose');

module.exports = mongoose.model(
	'Product',
	new mongoose.Schema(
		{
			title: {
				type: String,
				required: true,
			},
			description: {
				type: String,
				required: true,
			},
			images: [String],
			price: {
				type: Number,
				required: true,
			},
			category: {
				type: mongoose.SchemaTypes.ObjectId,
				ref: 'Category',
			},
			//    TODO: Add product characteristics
		},
		{
			timestamps: {
				createdAt: 'created_at',
				updatedAt: 'updated_at',
			},
		}
	)
);
