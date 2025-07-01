/*
Beecrowd exercise 1865.
Mjölnir.
Beginner.

https://www.urionlinejudge.com.br/judge/problems/view/1865
*/
package beecrowd

import "fmt"

func Mjolnir() {
	var N int
	fmt.Scan(&N)

	for range N {
		var name string
		var force int
		fmt.Scan(&name, &force)
		if name == "Thor" {
			fmt.Println("Y")
		} else {
			fmt.Println("N")
		}
	}
}
