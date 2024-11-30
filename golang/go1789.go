/*
Beecrowd exercise 1789.
The Race of Slugs.
Repetition
https://www.urionlinejudge.com.br/judge/problems/view/1789
*/

package beecrowd

import (
	"fmt"
)

func TheRaceOfSlugs() {
	var n, v int

	for {
		_, err := fmt.Scan(&n)
		if err != nil {
			break
		}

		var max int
		for i := 0; i < n; i++ {
			fmt.Scan(&v)
			if v > max {
				max = v
			}
		}

		if max < 10 {
			fmt.Println(1)
		} else if max < 20 {
			fmt.Println(2)
		} else {
			fmt.Println(3)
		}
	}
}
