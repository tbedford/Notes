// JavaScript snippets

"use strict";

var x = Math.floor(Math.random() * 10);     // returns a number between 0 and 9
console.log(x)


var a = Math.round(Math.random()*10)/10; // value between 0.0 and 1.0
console.log("a is: %f", a);


for (var i=0; i<1000; i++) {
    x = Math.floor((Math.random()*100)+1); // between 1 and 100
    //console.log(x);
    if (x >= 100){
        console.log("You won the prize! %d", x)
    }
}


function print_obj (o){
    console.log(o.name, o.age);
}

var t = {name: 'Tony', age: 55};
print_obj(t);
console.log(t.name);

let people = [];

people.push(t);
people.push({name: 'Fred', age: 23});

console.log(people.length);

for (var i=0; i<people.length; i++)
{
    print_obj(people[i]);

}

// random colours

  function rgb (r, g, b)
  {
      return "rgb(" + r + "," + g + "," + b + ")";
  }


  function random_color()
  {

      var r = Math.floor(Math.random() * 255);
      var g = Math.floor(Math.random() * 255);
      var b = Math.floor(Math.random() * 255);

      console.log ("r:%d g:%d b:%d",r,g,b);

      return rgb(r,g,b);
  }


for (var i=0; i<10;i++){
    console.log("Random color: %s", random_color());
}

function adjust_obj (obj){
    obj.x = obj.x +10;
}

var ob = {x: 1};
console.log(ob.x);
adjust_obj (ob);
console.log(ob.x);
