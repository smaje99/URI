/*
Beecrowd exercise 1180.

See: https://judge.beecrowd.com/es/problems/view/1180
*/

package beecrowd

import "fmt"

func LowestNumberAndPosition() {
	var N, X, minValue, position int
	var numbers []int

	fmt.Scanln(&N)

	for i := 0; i < N; i++ {
		fmt.Scanf("%d", &X)
		numbers = append(numbers, X)
	}

	minValue = numbers[0]
	position = 0
	for i := 1; i < N; i++ {
		if numbers[i] < minValue {
			minValue = numbers[i]
			position = i
		}
	}

	fmt.Printf("Menor valor: %d\nPosicao: %d\n", minValue, position)
}
