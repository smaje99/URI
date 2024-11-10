/*
Beecrowd exercise 1435.
Bidimensional Array

See: https://judge.beecrowd.com/es/problems/view/1435
*/

package beecrowd

import "fmt"

func SquareMatrixI() {
	var n int

	for {
		fmt.Scanln(&n)

		if n == 0 {
			break
		}

		// Create a bidimensional array

		matrix := make([][]int, n)

		for i := range matrix {
			matrix[i] = make([]int, n)
		}

		// Fill the matrix with values based on the layers.
		middle := n / 2

		if n % 2 != 0 {
			middle++
		}

		for i := 0; i < middle; i++ {
			bottom := n - i - 1

			for j := i; j <= bottom; j++ {
				matrix[i][j] = i + 1
				matrix[j][i] = i + 1
				matrix[bottom][j] = i + 1
				matrix[j][bottom] = i + 1
			}
		}

		// Print the matrix
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				if j == 0 {
					fmt.Printf("%3d", matrix[i][j])
				} else {
					fmt.Printf(" %3d", matrix[i][j])
				}
			}
			fmt.Println()
		}
		fmt.Println()
	}
}
