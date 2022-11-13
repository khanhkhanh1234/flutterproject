
  'use strict';
  
  if (process.env.NODE_ENV === "production") {
    module.exports = require("./DismissibleLayer.production.js");
  } else {
    module.exports = require("./DismissibleLayer.development.js");
  }
  