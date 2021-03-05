var mongoose = require('mongoose');
module.exports = mongoose.model('newb',{
  name: {type: String, default: 'Fresh eyes'}
});
