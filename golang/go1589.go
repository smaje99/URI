/*
Beecrowd exercise 1589.
Bob Conduit.
Repetition
https://www.urionlinejudge.com.br/judge/problems/view/1589
*/

package beecrowd

import (
	"fmt"
)

func BobConduit() {
	var t, r1, r2 int

	fmt.Scanln(&t)

	for i := 0; i < t; i++ {
		fmt.Scanln(&r1, &r2)
		fmt.Println(r1 + r2)
	}
}
