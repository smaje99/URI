/*
Beecrowd exercise 1564.
Brazil World Cup.
Repetition
https://www.urionlinejudge.com.br/judge/problems/view/1564
*/

package beecrowd

import (
	"fmt"
)

func BrazilWorldCup() {
	var n int

	for {
		_, err := fmt.Scanln(&n)

		if err != nil {
			break
		}

		if n == 0 {
			fmt.Println("vai ter copa!")
		} else {
			fmt.Println("vai ter duas!")
		}
	}
}
