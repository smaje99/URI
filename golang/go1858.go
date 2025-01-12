/*
Beecrowd exercise 1858.
Theon's Answer.
Beginner
https://www.urionlinejudge.com.br/judge/problems/view/1858
*/

package beecrowd

import (
	"fmt"
)

func TheonsAnswer() {
	var n, menor, position int
	fmt.Scanln(&n)

	var hits []int = make([]int, n)
	fmt.Scan(&hits[0])
	menor = hits[0]
	position = 1

	for i := 1; i < n; i++ {
		fmt.Scan(&hits[i])
		if hits[i] < menor {
			menor = hits[i]
			position = i + 1
		}
	}

	fmt.Println(position)
}
