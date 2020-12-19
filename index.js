var express = require('express');
var app = express();

//setting middleware
// app.use(express.static(__dirname + 'html')); //Serves resources from public folder

app.use('/', express.static(__dirname + '/frontend',{index: 'Home-Page.html'}));


var server = app.listen(9090, ()=>{
    console.log("running at port http://0.0.0:9090")
});