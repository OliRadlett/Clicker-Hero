var http = require('http');
var qs = require("query-string");
var request = require("requestify");

function processPost(request, response, callback) {
    var queryData = "";
    if(typeof callback !== 'function') return null;

    if(request.method == 'POST') {
        request.on('data', function(data) {
            queryData += data;
            if(queryData.length > 1e6) {
                queryData = "";
                response.writeHead(413, {'Content-Type': 'text/plain'}).end();
                request.connection.destroy();
            }
        });

        	request.on('end', function() {
            request.post = qs.parse(queryData);
            callback();
        });

    } else {
        response.writeHead(405, {'Content-Type': 'text/plain'});
        response.end();
    }
}

http.createServer(function(req, res) {

	res.write("Test");
	res.end();

	if (req.method == "POST") {

		processPost(req, res, function() {

			//console.log(req.post);
            var command = req.post.command;
            
            if (command == "analyse_money") {

                request.post("");

            }

			res.writeHead(200, "OK", {'Content-Type': 'text/plain'});
            res.end();

		});

	}

}).listen(1234);