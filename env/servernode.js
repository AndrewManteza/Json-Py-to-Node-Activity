var express = require('express');
var bodyParser = require('body-parser');
  
var app = express();
console.log('node server running')
  
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
  
app.post("/arraysum", (req, res) => {

    
    // Retrive array form post body
    var array = req.body.array;  
    

    sum = array.slice(0,3)
    
 
    // Calculate sum
    // var sum = 0;
    // for (var i = 0; i < array.length; i++) {
    //     if (isNaN(array[i])) {
    //         continue;

    //     }
    //     sum += array[i];
    // }
    // console.log(sum);
  
    // Return json response
    res.json({ result: sum});
});
  
// Server listening to PORT 3000
app.listen(3000);
