/*
Beecrowd exercise 1173.

See: https://judge.beecrowd.com/es/problems/view/1173
*/

package beecrowd

import "fmt"

func ArrayFillI() {
	var X[10] int
	var V int

	fmt.Scan(&V)

	if V < 50 {
		for i := 0; i < 10; i++ {
			X[i] = V
			V *= 2
		}

		for i := 0; i < 10; i++ {
			fmt.Printf("N[%d] = %d\n", i, X[i])
		}
	}
}
