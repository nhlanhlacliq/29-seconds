var location1 = 3;
var location2 = 4;
var location3 = 5;
var guess;
var hits = 0;
var guesses = 0;
var isSunk = false;

while (isSunk == false) {
  guess = prompt("Ready, aim, fire! (enter a number 0-6):");
  if (guess < 0 || guess > 6) {
    alert("Invalid guess");
  } else {
    guesses++;
    if (guess == location1 || guess == location2 || guess == location3) {
      hits++;
      alert("HM!");
      if (hits == 3) {
        isSunk = true;
        alert("You sunk my ship!");
      }
    }
  }
}
var userStats =
  guesses + " guesses to win," + " thus accuracy was: " + 3 / guesses;
alert("User stats");
