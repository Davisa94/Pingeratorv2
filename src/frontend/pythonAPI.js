function callMain(){
    var python = require("python-shell");
    var path = require("path");

    var options = {
        scriptPath : path.join(__dirname, '/../backend/'),
        pythonPath : "D:/Users/skyac/AppData/Local/Programs/Python/Python38-32/"
    };

    var mainloop = new python('main.py');
}