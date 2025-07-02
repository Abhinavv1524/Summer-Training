// document.write("Hello, World!");
// window.alert(
//   "You cant acess this page directly, please open it from the index.html file."
// );

// var name = prompt("What is your name?");
// if (name == "Abhinav") {
//   document.write("Hello, " + name + "!");
// } else if (name == "Abhi") {
//   document.write("Hello, " + name + "!");
// } else {
//   document.write("Hello, stranger!");
// }

/*
var age = prompt("What is your age?");
if (age >= 18) {
  document.write("You are ELIGIBLE FOR VOTE.");
} else if (age < 18) {
  document.write("You are NOT ELIGIBLE FOR VOTE.");
} else {
  document.write("Please enter a valid age.");
}
*/

// var score = prompt("Enter your score (0-100):");
// 40-50 Pass 50-60 just pass 60-70 excellent 70-80 very good 80-90 first class
/*
if (score >= 40 && score < 50) {
  document.write("You have passed.");
} else if (score >= 50 && score < 60) {
  document.write("You have just passed.");
} else if (score >= 60 && score < 70) {
  document.write("You have excellent score.");
} else if (score >= 70 && score < 80) {
  document.write("You have very good score.");
} else if (score >= 80 && score < 90) {
  document.write("You have first class score.");
} else if (score >= 90 && score <= 100) {
  document.write("You have outstanding score.");
} else if (score < 0 || score > 100) {
  document.write("Please enter a valid score between 0 and 100.");
}
*/

// switch case wtth months name that say welcome that that mmonth
/*
var month = prompt("Enter the month name:");
switch (month) {
  case "January":
    document.write("Welcome to January!");
    break;
  case "February":
    document.write("Welcome to February!");
    break;
  case "March":
    document.write("Welcome to March!");
    break;
  case "April":
    document.write("Welcome to April!");
    break;
  case "May":
    document.write("Welcome to May!");
    break;
  case "June":
    document.write("Welcome to June!");
    break;
  case "July":
    document.write("Welcome to July!");
    break;
  case "August":
    document.write("Welcome to August!");
    break;
  case "September":
    document.write("Welcome to September!");
    break;
  case "October":
    document.write("Welcome to October!");
    break;
  case "November":
    document.write("Welcome to November!");
    break;
  case "December":
    document.write("Welcome to December!");
    break;
  default:
    document.write("Please enter a valid month name.");
    break;
}
*/
// function in js
// function greet(name) {
//   return "Hello, " + name + "!";
// }
// // Example usage
// var userName = prompt("Enter your name:");
// var greetingMessage = greet(userName);
// document.write(greetingMessage);

// // function that take a,b,c
// function value(a, b, c) {
//   document.write("A: " + a + " B: " + b + " C: " + c);
// }
// value(10, 20)

// addition of two Number
// function add(a, b) {
//   document.write("Sum: of " + a + " and " + b + " is: " + (a + b) + "<br>");
// }
// add(5, 10);

// function with 2 parameters and call 3 values

function value(a, b) {
  document.write("A: " + a + " B: " + b + "<br>");
}
value(10, 20, 30);

// args
function args(...args) {
  document.write("Arguments: " + args.join(", ") + "<br>");
}
args(1, 2, 3, 4, 5);

// minimum 1 argument
function minArg(a, ...args) {
  document.write("First argument: " + a + "<br>");
  document.write("Additional arguments: " + args.join(", ") + "<br>");
}
minArg(10, 20, 30, 40, 50);
