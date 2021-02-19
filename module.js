exports.myDateTime = function()
{
	return Date();
};

//testing: module declration of a return example case: .stringify

exports.getMe = function()
{
	var myObj = {name:"Caleb", age:"31", city:"Redlands"};
	var myJSON = JSON.stringify(myObj);
	return myJSON;
};
