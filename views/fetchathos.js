var fetch = require('node-fetch');
var url = "https://api.sunrise-sunset.org/json?lat=40.23810&lng=24.20133&date=today";

    
var getData = async url =>
{
        try 
        {
                var response = await fetch(url);
                var json = await response.json();
                var data = JSON.parse(json);
                return data;
        }
        catch (error)
        {
                console.log(error);
        }
};
getData(url);

    
