/*
Beecrowd exercise 1828.
Bazinga!.
None
https://www.urionlinejudge.com.br/judge/problems/view/1828
*/

package beecrowd

import (
	"fmt"
)

func Bazinga() {
	var n int
	var sheldon, raj string

	fmt.Scan(&n)

	for i := 1; i <= n; i++ {
		fmt.Scan(&sheldon, &raj)

		if sheldon == raj {
			fmt.Printf("Caso #%d: De novo!\n", i)
		} else if (sheldon == "tesoura" && (raj == "papel" || raj == "lagarto")) ||
			(sheldon == "papel" && (raj == "pedra" || raj == "Spock")) ||
			(sheldon == "pedra" && (raj == "lagarto" || raj == "tesoura")) ||
			(sheldon == "lagarto" && (raj == "Spock" || raj == "papel")) ||
			(sheldon == "Spock" && (raj == "tesoura" || raj == "pedra")) {
			fmt.Printf("Caso #%d: Bazinga!\n", i)
		} else {
			fmt.Printf("Caso #%d: Raj trapaceou!\n", i)
		}
	}
}
