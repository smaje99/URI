/*
Beecrowd exercise 2006.
Identifying Tea.
Beginner
https://www.urionlinejudge.com.br/judge/problems/view/2006
*/

package beecrowd

import (
	"fmt"
)

func IdentifyingTea() {
	var tea, guess, count int

	fmt.Scanf("%d", &tea)

	for range 5 {
		fmt.Scanf("%d", &guess)
		if guess == tea {
			count++
		}
	}

	fmt.Println(count)
}
