//modules
const express = require('express');
const app = express();
//new to mongodb need training wheels
var mongoose = require('mongoose');


//set port
const port = 3000;
//config files db path defined
var db = require('./config/db');
console.log("connecting....",db);
//connect to local db at alternate port to site

  //stuff here for CRUD

mongoose.connect(db.url,{
  useNewUrlParser: true,
  useUnifiedTopology: true,
  useCreateIndex: true,
  useFindAndModify:false
});


//Home Route
app.get('/', (req,res) => res.send('Here is HOME'));

//define Route
app.get('/newb', function (req,res){
  res.send('Newb List: ');
});

//sampling api Route
//grab the newb we just created
var newb = require('./app/models/newb');
app.get('/api/newbs', function(req,res){
  //using mongoose to get newb
  newb.find(function(err,newbs){
    if(err)
      res.send(err);
    res.json(newbs);
  });
});


//startup app at localhost:3000
app.listen(port,() => console.log('App is listening on port 3000!'));
