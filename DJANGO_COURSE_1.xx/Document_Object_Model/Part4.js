var restart = document.querySelector("#b");
var squares = document.querySelectorAll("td");

function res() {
for (let i = 0; i < squares.length; i++) {
    squares[i].textContent = "";
    
    }
}
restart.addEventListener("click", res)

function x() {
    if (this.textContent == '') {
        this.textContent = 'X';
    } else if (this.textContent == 'X') {
        this.textContent = 'O';
    } else {
        this.textContent = ''
    }
}

for (let i = 0; i < squares.length; i++) {
    squares[i].addEventListener("click", x);
    
}
