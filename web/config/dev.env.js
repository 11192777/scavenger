'use strict'
const merge = require('webpack-merge')
const prodEnv = require('./prod.env')
const USER_AUTHORITY = {
  orgServer: true
}

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
  BASE_API: '"http://192.168.1.104:9999"',
})
