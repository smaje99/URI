/*
Beecrowd exercise 1190.
Bidimensional Array

See: https://judge.beecrowd.com/es/problems/view/1190
*/

package beecrowd

import "fmt"

func RightArea() {
	var (
		operation 	string
		sum 				float64 = 0.0
		matrix			[12][12]float64
		result			float64
	)

	fmt.Scanln(&operation)

	for i := 0; i < 12; i++ {
		for j := 0; j < 12; j++ {
			fmt.Scanln(&matrix[i][j])

			if i < j && i > 11 - j {
				sum += matrix[i][j]
			}
		}
	}

	result = sum

	if operation == "M" {
		result /= 30.0
	}

	fmt.Printf("%.1f\n", result)
}