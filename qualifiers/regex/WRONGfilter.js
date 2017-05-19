var fs = require('fs'),
    readline = require('readline');

var rd = readline.createInterface({
    input: fs.createReadStream('./pass.lst'),
    console: false
});


var mediumRegex = new RegExp("^[wW][aeE](?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*]{1})(?=.{8,})");

rd.on('line', function(line) {
    if (mediumRegex.test(line)){
       console.log(line)
    }
});


