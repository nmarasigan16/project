var express = require('express')
var mongoose = require('mongoose')
var router_base = require('./routes/base')
var router_realtime_update = require('./routes/realtime_update');
var app = express()
var server = require('http').Server(app);

var sockets = [];

app.use('/', express.static('../frontend'))

app.use('/base', router_base)
app.use('/realtime', router_realtime_update)
//realtime

var io = require('socket.io')(server)

io.on('connection', function(socket){
	sockets.push(socket)
	console.log('a user connected');
});

//Not app.listen
server.listen(8089, "127.0.0.1", function(){
	console.log("Started");
})