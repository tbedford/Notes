// JavaScript snippets

"use strict";

var x = Math.floor(Math.random() * 10);     // returns a number between 0 and 9
console.log(x)


for (var i=0; i<1000; i++) {
    x = Math.floor((Math.random()*100)+1); // between 1 and 100
    //console.log(x);
    if (x >= 100){
        console.log("You won the prize! %d", x)
    }
}

var obj = {
    name: 'Tony',
    age: 55
};

function print_obj (o){
    console.log(o.name, o.age);
}

print_obj(obj);

let people = [];

people.push(obj);
people.push({name: 'Fred', age:23});

console.log(people.length);

for (var i=0; i<people.length; i++)
{
    print_obj(people[i]); 

}





