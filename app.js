const express = require('express'); //require express
var app = express(); //create instance of express app
var port = process.env.port || 3000; //define port
var bodyParser = require('body-parser');

const options = {
    apiKey: '47559095d486028e154d6fb8739c88a9b07275b54b35080b9020d439d67ba670',  // use your sandbox app API key for development in the test environment
    username: 'sandbox',      // use 'sandbox' for development in the test environment
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

//create random verification code
function randomInRange(from, to) {
    var r = Math.random();
    return Math.floor(r * (to - from) + from);
}
var verify = randomInRange()
app.post('/', function(request, response){
    // Use the service
    const moses = {    //moses is just an example
        to:  request.body.phone,
        message: `Your verification code is : ${randomInRange(1,10000)}`
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
app.post('/verify', function(request, response){
    var verificationCode = request.body.verification;
    if (verificationCode === verify) {
        response.statusCode(200);
    }else {
        response.redirect('/');
    }
});

app.listen(port, () => {
    console.log(`App running on port ${port}`);
})