/*
Beecrowd exercise 1164.

See: https://judge.beecrowd.com/es/problems/view/1164
*/

package beecrowd

import (
	"fmt"
	"math"
)

func isPerfectNumber(num int) bool {
	if num < 6 {
		return false
	}

	sum := 0

	for i := 1; i <= int(math.Sqrt(float64(num))); i++ {
		if num % i == 0 {
			if num == num / i {
				sum += i
			} else {
				sum += i + num / i
			}
		}
	}

	return num == sum
}

func main() {
	var nCases int

	fmt.Scan(&nCases)

	if 1 <= nCases && nCases <= 100 {
		for i := 0; i < nCases; i++ {
			var number int

			fmt.Scan(&number)

			if 1 <= number && number <= 100_000_000 {
				if isPerfectNumber(number) {
					fmt.Printf("%d eh perfeito\n", number)
				} else {
					fmt.Printf("%d nao eh perfeito\n", number)
				}
			}
		}
	}
}
