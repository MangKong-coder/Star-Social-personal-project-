var fname = prompt("Welcome! Enter your First Name: ");
var lname = prompt("Welcome! Enter your Last Name: ");
var age = prompt("Welcome! Enter your Age: ");
var cm = prompt("Welcome! Enter your height in cm: ");
var pet = prompt("Welcome! Enter your Pet's Name: ");

var name = null
var old = null
var hei = null
var docat = null

if (fname[0] === lname[0]) {
    name = true;
} else {
    name = false;
};

if (age > 20 && age < 30 ) {
    old = true;
} else {
    old = false;
};

if ( cm >= 170 ) {
    hei = true;
} else {
    hei = false;
};

if (pet[pet.length-1] === "y") {
    docat = true;
} else {
    docat = false;
};

if (name && old && hei && docat) {
    console.log("Hi Spy! WelCum to the Gulag!");
} else {
    console.log("Nothing to see here!");
}
