const express = require('express'); //require express
var app = express(); //create instance of express app
var port = process.env.port || 3000; //define port

//get path
var path = require('path')

//view engine (css images and static files)
app.set('views', path.join(__dirname, 'views'));
app.use('/static', express.static('static'))

app.use(express.static('views'));

app.listen(port, () => {
    console.log(`App running on port ${port}`);
})
