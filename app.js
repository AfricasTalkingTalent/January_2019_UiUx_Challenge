const express = require('express'); //require express
var app = express(); //create instance of express app
var port = process.env.port || 3000; //define port
var bodyParser = require('body-parser');

const options = {
    apiKey: '29d37ee7b679d71bf33600efc9272ad278f7b42d7cd45ee5943bcbe283874d73',  // use your sandbox app API key for development in the test environment
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

//redirect to verification page
app.use(express.static(__dirname + "/views/verification.html"));
app.get('/verify', function(req, res) {
    res.sendFile(__dirname + "/views/verification.html");
  });

app.post('/', function(request, response){
    // Use the service
    const moses = {
        to:  request.body.phone,
        message: "Hello, it's Samuel Barasa."
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
    response.redirect('/verify');
});

app.listen(port, () => {
    console.log(`App running on port ${port}`);
})