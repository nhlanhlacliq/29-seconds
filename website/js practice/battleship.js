var location1 = Math.floor(Math.random() * 5);
var location2 = location1++;
var location3 = location2++;
var guess;
var hits = 0;
var guesses = 0;
var isSunk = false;

while (!isSunk) {
  guess = prompt("Ready, aim, fire! (enter a number 0-6):");
  if (guess < 0 || guess > 6) {
    alert("Invalid guess");
  } else {
    guesses++;
    if (guess == location1 || guess == location2 || guess == location3) {
      hits++;
      alert("HIT!");
      if (hits == 3) {
        isSunk = true;
        alert("You sunk my ship!");
      }
    } else {
      alert("MISS");
    }
  }
}

var userStats =
  "You took " +
  guesses +
  " guesses to win." +
  " Accuracy: " +
  Math.round((3 / guesses) * 100, 2) +
  "%";

alert(userStats);
