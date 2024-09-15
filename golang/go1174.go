/*
Beecrowd exercise 1174.

See: https://judge.beecrowd.com/es/problems/view/1174
*/

package beecrowd

import "fmt"

func ArraySelectionI() {
	var A[100] float64

	for i := 0; i < 100; i++ {
		fmt.Scan(&A[i])
	}

	for i := 0; i < 100; i++ {
		if A[i] <= 10 {
			fmt.Printf("A[%d] = %.1f\n", i, A[i])
		}
	}
}
