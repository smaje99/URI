/*
Beecrowd exercise 1827.
Square Matrix IV.
Bidimensional Array
https://www.urionlinejudge.com.br/judge/problems/view/1827
*/

package beecrowd

import (
	"fmt"
)

func SquareMatrixIV() {
	var n int

	for {
		_, err := fmt.Scan(&n)

		if err != nil {
			break
		}

		inside := n / 3
		middle := n / 2

		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				if i == middle && j == middle {
					fmt.Print(4)
				} else if i >= inside && i < n-inside && j >= inside && j < n-inside {
					fmt.Print(1)
				} else if i == j {
					fmt.Print(2)
				} else if i+j == n-1 {
					fmt.Print(3)
				} else {
					fmt.Print(0)
				}
			}
			fmt.Println()
		}
		fmt.Println()
	}
}
