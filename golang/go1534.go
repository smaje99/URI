/*
Beecrowd exercise 1534.
Bidimensional Array

See: https://judge.beecrowd.com/es/problems/view/1534
*/

package beecrowd

import (
	"fmt"
	"io"
)

func Array123() {
	var n int

	for {
		_, err := fmt.Scanln(&n)

		if err == io.EOF {
			break
		}

		if n < 3 || n > 70 {
			continue
		}

		// Generate and print the matrix
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				if (i == j && i + j == n - 1) || i + j == n - 1 {
					fmt.Print("2")
				} else if i == j {
					fmt.Print("1")
				} else {
					fmt.Print("3")
				}
			}
			fmt.Println()
		}
	}
}
