// var scoops = 5;

// while (scoops > 0) {
//   console.log("SCOOP!<br>");
//   scoops -= 1;

//   if (scoops < 3) {
//     alert("Ice cream running low");
//   }
// }

var name = "Joe";
var i = 0;

while (i < 2) {
  document.write("Happy Birthday to you.<br>");
  i++;
}
document.write("Happy Birthday dear " + name + ",<br>");
document.write("Happy Birthday to you.<br>");

var word = "bottles";
var count = 99;

while (count > 0) {
  document.write(count + " " + word + " of beer on the wall<br>");
  document.write(count + " " + word + " of beer,<br>");
  document.write("Take one down, pass it around,<br>");
  count = count - 1;

  if (count < 1) {
    document.write("No more " + word + " of beer on the wall.");
  }
}
