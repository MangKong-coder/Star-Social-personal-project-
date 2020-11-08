// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array
function addNew() {
    var name = prompt("What name would you like to add?")
    roster.push(name);
    
}

// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster
function remove() {
    var name = prompt("What name would you like to remove from the roster?");
    var ind = roster.indexOf(name);
    roster.splice(ind, 1);
    
}

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

// DISPLAY ROSTER

// Create a function called display that prints out the orster to the console.
function display() {
    console.log(roster);
    
}

// Start by asking if they want to use the web app
var yn = prompt("Would you like to try the web app? y/n")
var yu = "oh yeah"
// Now create a while loop that keeps asking for an action (add,remove, display or quit)
if (yn === "y") {
    while(yu !== "quit") {
        var action = prompt("Would you like to add, remove, display or quit?");

        if (action === "add") {
            addNew();
        } else if (action === "remove") {
            remove();
        } else if (action === "display") {
            display();
        } else if (action === "quit") {
            yu = "quit";
        }
}
}
    
// Use if and else if statements to execute the correct function for each command.
