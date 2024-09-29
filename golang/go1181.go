/*
Beecrowd exercise 1181.

See: https://judge.beecrowd.com/es/problems/view/1181
*/

package beecrowd

import "fmt"

func LineInArray() {
	var line int
	var operation string
	var sum float64
	var matrix [12][12]float64

	fmt.Scanln(&line)
	fmt.Scanln(&operation)

	if line > 0 && line < 12 && operation == "S" || operation == "M" {
		for i := 0; i < 12; i++ {
			for j := 0; j < 12; j++ {
				fmt.Scanln(&matrix[i][j])
			}
		}

		for i := 0; i < 12; i++ {
			sum += matrix[line][i]
		}

		if operation == "S" {
			fmt.Printf("%.1f\n", sum)
		} else {
			fmt.Printf("%.1f\n", sum / 12)
		}
	}
}
