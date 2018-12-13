const express = require('express'); //require express
var app = express(); //create instance of express app
var port = process.env.port || 3000; //define port
var bodyParser = require('body-parser');

//get path
var path = require('path')

//view engine (css images and static files)
app.set('views', path.join(__dirname, 'views'));
app.use('/static', express.static('static'))
app.use(express.static('views'));

app.use(bodyParser.urlencoded({ extended: true })); 

//create an empty array that will store the data after submission
let details = [];

app.post('/', function(request, response){
    details.push(request.body.username);
    details.push(request.body.phone);
    details.push(request.body.password);
    console.log(details) 
    response.end();   
});

app.listen(port, () => {
    console.log(`App running on port ${port}`);
})
