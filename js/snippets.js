// JavaScript snippets

var x = Math.floor(Math.random() * 10);     // returns a number between 0 and 9
console.log(x)


for (i=0; i<1000; i++) {
    x = Math.floor((Math.random()*100)+1); // between 1 and 100
    //console.log(x);
    if (x >= 100){
        console.log("You won the prize! %d", x)
    }
}


