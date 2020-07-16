var express = require("express");
var theapp = express();
theapp.use(express.static('public'))

theapp.get("/url", (req, res, next) => {
 res.json(["this","is","my","test","server"]);
});

//all the records returned
theapp.get('/all', function (req, res) {
	//check that the keys exist
	if(!obj.hasOwnProperty(req.params["maken"])){
		res.send();
		return;
	}
	my_res = obj[req.params["maken"]][req.params["modeln"]];
	//res.send(req.params["maken"])
	//	res.send(req.params)
	res.send(my_res);
})

//just some of the records returned
theapp.get('/stuff', function (req, res) {
	res.send(my)
})

theapp.listen(3001, () => {
 console.log("Server running on port 3001");
});


