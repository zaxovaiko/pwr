const mongoose = require('mongoose');

module.exports = mongoose.model('Transaction', new mongoose.Schema({
    user_id: {
        type: mongoose.SchemaTypes.ObjectId,
        ref: 'User'
    },
    product_id: {
        type: mongoose.SchemaTypes.ObjectId,
        ref: 'Product'
    },
    count: {
        type: Number,
        required: true
    },
    status: {
        type: String,
        required: true
    }
}, {
    timestamps: {
        createdAt: 'created_at',
        updatedAt: 'updated_at'
    },
}))
