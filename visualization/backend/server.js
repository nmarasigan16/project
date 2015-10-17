var express = require('express')
var mongoose = require('mongoose')
var router_base = require('./routes/base')
var router_realtime_update = require('./routes/reatime_update');

var app = express()

app.use('/base', router_base)
app.use('/realtime', router_realtime_update)
// /realtime

app.listen(8089)