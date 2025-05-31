/* function sum(a, b) {
    return a + b; // poprawka błędu -> PATCH
  } -- TAK BYLO DLA PATCH
*/

function sum(...numbers) {
  return numbers.reduce((acc, n) => acc + n, 0);
}  // tak jest dla MAJOR

function multiply(a, b) {
    return a * b;
  } // A TO DLA MINOR