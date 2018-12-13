const express = require('express'); //require express
var app = express(); //create instance of express app
var port = process.env.port || 3000; //define port
var bodyParser = require('body-parser');

const options = {
    apiKey: '85e656dc062f647943301407869f4289d5955b10590b9417b5932dbbcfab53e9',  // use your sandbox app API key for development in the test environment
    username: 'samuelbarasa',      // use 'sandbox' for development in the test environment
};
const AfricasTalking = require('africastalking')(options);

// Initialize a service e.g. SMS
sms = AfricasTalking.SMS

//get path
var path = require('path')

//view engine (css images and static files)
app.set('views', path.join(__dirname, 'views'));
app.use('/static', express.static('static'))
app.use(express.static('views'));

app.use(bodyParser.urlencoded({ extended: true })); 

app.post('/', function(request, response){
    // Use the service
    const moses = {
        to:  request.body.phone,
        message: "I'm a lumberjack and its ok, I work all night and sleep all day"
    }
    // Send message and capture the response or error
    sms.send(moses)
        .then( res => {
            console.log(res);
            response.sendStatus(200);
        })
        .catch( error => {
            console.log(error);
            response.sendStatus(401);
            });
        });

app.listen(port, () => {
    console.log(`App running on port ${port}`);
})