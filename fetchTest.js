//nodeFetch test tutorial valentinog.com/blog/http-js/ 
//Location of choice: St Panteleimon Monastery Mt. Athos, Greece.
var fetch = require('node-fetch');
var url = "https://api.sunrise-sunset.org/json?lat=40.23810&lng=24.20133&date=today";

var getData = async url =>
{
	try 
	{
		var response = await fetch(url);
		var json = await response.json();
		console.log(json);
	}
	catch (error)
	{
		console.log(error);
	}
};
getData(url);

