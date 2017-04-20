// v 0.0.01
// xuxiang
// 2017-03-21
 // FServer.js    
var fs   = require('fs');    
var mime = require('mine').mime;    
function filesLoad(filePath, type, req, res){    
    fs.exists(filePath, function(exists){    
        if ( !exists ) {    
            res.writeHead(404, {'Content-Type': 'text/plain'});    
            // res.write();    
            res.end();    
        } else {    
            fs.readFile(filePath, 'binary', function(err, file){    
                if ( err ) {    
                    res.writeHead(500, {'Content-Type': 'text/plain'});    
                    // res.write();    
                    res.end();    
                } else {    
                    res.writeHead(200, {'Content-Type': mime[type]});    
                    res.write(file, 'binary');    
                    res.end();    
                }    
            });    
        }    
    })    
}    
exports.filesLoad = filesLoad;   