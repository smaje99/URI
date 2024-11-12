/*
Beecrowd exercise 1478.
Bidimensional Array

See: https://judge.beecrowd.com/es/problems/view/1478
*/

package beecrowd

import (
	"fmt"
	"math"
)

func SquareMatrixII() {
	var n int

	for {
		_, err := fmt.Scanln(&n)

		if err != nil || n == 0 {
			break
		}

		// Generate and print the matrix
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				value := int(math.Abs(float64(i - j))) + 1

				if j == 0 {
					fmt.Printf("%3d", value)
				} else {
					fmt.Printf(" %3d", value)
				}
			}
			fmt.Println()
		}
		fmt.Println()
	}
}
