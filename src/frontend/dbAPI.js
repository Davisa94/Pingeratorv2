

function getDBCredentials(){
    console.log("prepping file")
    var path = require('path');
    credsFile = path.join(__dirname, '../backend/dbcredentials.json');
    // console.log(credsFile);
    var fs = require('fs');
    var creds = fs.readFileSync(credsFile, 'utf8');
    // console.log(creds);
    return creds;
}

function dbConnect(){
    var mysql = require('mysql2');
    var creds = getDBCredentials();
    var creds_obj = JSON.parse(creds);
    var hostname = "localhost";
    var username = creds_obj.user;
    var schema = "pingerator"
    // console.warn(`\n\n\n\n\n\n\n\n\n\n\n\nUSERNAME: ${username}`);
    var pass = creds_obj.password;
    var connection = mysql.createConnection({
        host: hostname,
        user: username,
        password: pass,
        database: schema
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
    query = connection.query(sql, function(err, rows, fields) {
        console.log(fields)
       for(row in rows){
           console.log(row);
       }
        // console.log(colNames)

      });
    console.log(query.sql);
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