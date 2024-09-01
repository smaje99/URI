/*
Beecrowd exercise 1164.

See: https://judge.beecrowd.com/es/problems/view/1164
*/

package beecrowd

import "fmt"

func ArrayReplacementI() {
	var X[10] int

	for i := 0; i < 10; i++ {
		fmt.Scan(&X[i])

		if X[i] <= 0 {
			X[i] = 1
		}
	}

	for i := 0; i < 10; i++ {
		fmt.Printf("X[%d] = %d\n", i, X[i])
	}
}
