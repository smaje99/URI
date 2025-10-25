/*
Beecrowd exercise 1962.
A Long, Long Time Ago.
Beginner.
Ad-Hoc, Repetition.

https://www.urionlinejudge.com.br/judge/problems/view/1962
*/

package beecrowd

import (
	"bufio"
	"fmt"
	"os"
)

func ALongLongTimeAgo() {
	in := bufio.NewReader(os.Stdin)

	var N int
	fmt.Fscan(in, &N)

	for i := 0; i < N; i++ {
		var T int
		fmt.Fscan(in, &T)

		year := 2015 - T

		if year > 0 {
			fmt.Printf("%d D.C.\n", year)
		} else {
			fmt.Printf("%d A.C.\n", -year+1)
		}
	}
}
