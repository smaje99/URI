/*
Beecrowd exercise 1182.

See: https://judge.beecrowd.com/es/problems/view/1182
*/

package beecrowd

import "fmt"

func ColumnInArray() {
	var column int
	var operation string
	var sum float64
	var matrix [12][12]float64

	fmt.Scanln(&column)
	fmt.Scanln(&operation)

	if column > 0 && column < 12 && operation == "S" || operation == "M" {
		for i := 0; i < 12; i++ {
			for j := 0; j < 12; j++ {
				fmt.Scanln(&matrix[i][j])
			}
		}

		for i := 0; i < 12; i++ {
			sum += matrix[i][column]
		}

		if operation == "S" {
			fmt.Printf("%.1f\n", sum)
		} else {
			fmt.Printf("%.1f\n", sum / 12)
		}
	}
}
