/*
Beecrowd exercise 1557.
Square Matrix III.
Bidimensional Array

See: https://judge.beecrowd.com.br/judge/problems/view/1557
*/

package beecrowd

import (
	"fmt"
)

func SquareMatrixIII() {
	var n int

	for {
		_, err := fmt.Scanln(&n)

		if err != nil || n == 0 {
			break
		}

		// Calculate the maximum value in the matrix and its width
		maxValue := 1 << uint(2 * n - 2)
		maxWidth := len(fmt.Sprintf("%d", maxValue))

		// Generate and print the matrix
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				value := 1 << uint(i+j)

				if j == 0 {
					fmt.Printf("%*d", maxWidth, value)
				} else {
					fmt.Printf(" %*d", maxWidth, value)
				}
			}
			fmt.Println()
		}
		fmt.Println()
	}
}
