var express = require('express')
var router = express.Router()

function modelSetup(){
	
}

router.get('/', function(req, res){
	res.send("realtime update")
})

router.post('/', function(req, res){
	res.send("Real time post request")
})

module.exports = router