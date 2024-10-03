/*
Beecrowd exercise 1183.

See: https://judge.beecrowd.com/es/problems/view/1183
*/

package beecrowd

import "fmt"

func AboveTheMainDiagonal() {
	var (
		operation 	string
		sum 				float64
		matrix			[12][12]float64
		result			float64
	)

	fmt.Scanln(&operation)

	for i := 0; i < 12; i++ {
		for j := 0; j < 12; j++ {
			fmt.Scanln(&matrix[i][j])
		}
	}

	for i := 0; i < 12; i++ {
		for j := i + 1; j < 12; j++ {
			sum += matrix[i][j]
		}
	}

	result = sum

	if operation == "M" {
		result /= 66
	}

	fmt.Printf("%.1f\n", result)
}
