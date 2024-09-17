/*
Beecrowd exercise 1175.

See: https://judge.beecrowd.com/es/problems/view/1175
*/

package beecrowd

import "fmt"

func ArrayChangeI() {
	var N [20]int

	for i := 0; i < 20; i++ {
		fmt.Scan(&N[i])
	}

	for i := 0; i < 10; i++ {
		N[i], N[19 - i] = N[19 - i], N[i]
	}

	for index, value := range N {
		fmt.Printf("N[%d] = %d\n", index, value)
	}
}
