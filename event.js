let result = document.getElementById("result");

function add() {
    let num1 = parseInt(document.getElementById("num1").value);
    let num2 = parseInt(document.getElementById("num2").value);
    console.log("Adding " + num1 + " and " + num2);
    result.innerText = "Addition: " + (num1 + num2);
}

function subtract() {
    let num1 = parseInt(document.getElementById("num1").value);
    let num2 = parseInt(document.getElementById("num2").value);
    console.log("Subtracting " + num1 + " and " + num2);
    result.innerText = "Subtraction: " + (num1 - num2);
}

function multiply() {
    let num1 = parseInt(document.getElementById("num1").value);
    let num2 = parseInt(document.getElementById("num2").value);
    console.log("Multiplying " + num1 + " and " + num2);
    result.innerText = "Multiplication: " + (num1 * num2);
}