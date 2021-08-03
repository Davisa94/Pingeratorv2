

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
    var mysql = require('mysql');
    var creds = getDBCredentials();
    var hostname = "localhost";
    var username = creds.user;
    var pass = creds.password;
    var connection = mysql.createConnection({
        host: hostname,
        user: username,
        password: pass,
    });
    connection.connect(function(err){
        if(err){
            console.log(`Issue connecting to the Database: ${err}`)
        }
    })
    return connection;
}

function getRecentPings(connection){
    let sql = `SELECT * FROM ping ORDER BY datetime_tested DESC LIMIT 3`;
    query = connection.query(sql);
    console.log(query);
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
module.exports = { dbApi, getDBCredentials, dbConnect, getRecentPings }