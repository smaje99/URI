/*
Beecrowd exercise 1957.
Convert to hexadecimal.
Beginner.
Ad-Hoc, Printf Options.

https://www.urionlinejudge.com.br/judge/problems/view/1957
*/

package beecrowd

import "fmt"

func ConvertToHexadecimal() {
	var n int
	fmt.Scan(&n)
	fmt.Printf("%X\n", n) // %X prints in uppercase hexadecimal
}
