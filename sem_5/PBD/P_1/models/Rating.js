const mongoose = require('mongoose');

module.exports = mongoose.model('Rating', new mongoose.Schema({
    user_id: {
        type: mongoose.SchemaTypes.ObjectID,
        required: true
    },
    product_id: {
        type: mongoose.SchemaTypes.ObjectID,
        required: true
    },
    stars: {
        type: Number,
        required: true
    }
}, {
    timestamps: {
        createdAt: 'created_at',
        updatedAt: 'updated_at'
    },
}))
