/*
Beecrowd exercise 1541.
Bidimensional Array

See: https://judge.beecrowd.com/es/problems/view/1541
*/

package beecrowd

import (
	"fmt"
	"math"
)

func BuildingHouses() {
	var side1, side2, percentage int

	for {
		_, err := fmt.Scanln(&side1, &side2, &percentage)

		if err != nil || side1 == 0 {
			break
		}

		if side1 < 1 || side1 > 1000 || side2 < 1 || side2 > 1000 || percentage < 1 || percentage > 1000 {
			continue
		}

		fmt.Println(int(math.Sqrt(float64(side1 * side2 * 100 / percentage))))
	}
}
