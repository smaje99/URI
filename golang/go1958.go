/*
Beecrowd exercise 1958.
Scientific Notation.
Beginner.
Ad-Hoc, Printf Options.

https://www.urionlinejudge.com.br/judge/problems/view/1958
*/

package beecrowd

import "fmt"

func ScientificNotation() {
	var n float64
	fmt.Scan(&n)
	fmt.Printf("%+.4E\n", n) // Prints the number in scientific notation
}
