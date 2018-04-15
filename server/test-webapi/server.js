var express = require("express");
var PythonShell = require("python-shell");
var process = require('process');
process.chdir('../clicker-hero/bot');
var pyshell = new PythonShell("script.py");

pyshell.on("message", function(message) {

    console.log("Recieved ", message);

});

var app = express();

app.get("/", function(req, res) {

	res.end("Connected.");

});

app.get("/test", function(req, res) {

	res.end("Test!");

});

app.get("/test", function(req, res) {

	console.log("Sending command to bot");
    pyshell.send("get_money");

});


var server = app.listen(1234, "192.168.1.144", function() {

	var host = server.address().address;
	var port = server.address().port;

	console.log("API running on: http://%s:%s", host, port);

});