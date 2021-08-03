

function printCreds(){
    console.log("prepping file")
    var path = require('path');
    var credentials;
    credsFile = path.join(__dirname, '../backend/creds.json');
    console.log(credsFile);
    var fs = require('fs');
    var creds = await fs.readFile(credsFile, 'utf8', function (err, data) {
        if (err) return console.log(err);
        credentials = data;
        return data
      });
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
module.exports = { dbApi, printCreds }