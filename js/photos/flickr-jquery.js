
var pluginName = "flickr-gallery",
  defaults = {
    api_key: '2dd9be651d5db029e6444515a0fa3868',
    user_id: '131652881@N03'
    loadingSpeed: 38
  },
  api_url = 'https://api.flickr.com/services/rest/',
  photos = [];

function Plugin(element, options) {
  this.element = $(element);
  this.settings = $.extend({}, defaults, options);
  this._defaults = defaults;
  this._name = pluginName;

  
  
}