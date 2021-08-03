var mysql = require('mysql');
var connection =

function getDBCredentials(){
    console.log("prepping file")
    var path = require('path');
    credsFile = path.join(__dirname, '../backend/creds.json');
    console.log(credsFile);
    var fs = require('fs');
    var creds = fs.readFileSync(credsFile, 'utf8');
    console.log(creds);
}

function dbConnect(){
    return 0;
}


function dbApi()
{
    const {PythonShell} = require('python-shell');

    let pyshell = new PythonShell('../backend/dbAPI.py');

    pyshell.send(JSON.stringify([10]))

    pyshell.on('message', function(message) {
    console.log(message);
    })

    pyshell.end(function (err) {
    if (err){
        throw err;
    };
    console.log('finished');
    });
};
module.exports = { dbApi, getDBCredentials }