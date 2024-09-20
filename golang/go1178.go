/*
Beecrowd exercise 1178.

See: https://judge.beecrowd.com/es/problems/view/1178
*/

package beecrowd

import "fmt"

func ArrayFillIII() {
	var Y float64

	fmt.Scan(&Y)

	for i := 0; i < 100; i++ {
		fmt.Printf("N[%d] = %.4f\n", i, Y)
		Y /= 2
	}
}
