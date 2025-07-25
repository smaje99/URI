/*
Beecrowd exercise 1837.
Preface.
Ad-hoc.
Beginner.

https://www.urionlinejudge.com.br/judge/problems/view/1837
*/

package beecrowd

import (
	"fmt"
	"math"
)

func Preface() {
	var a, b int
	fmt.Scan(&a, &b)

	absB := int(math.Abs(float64(b)))

	q := a / absB
	r := a % absB

	if a < 0 && r != 0 {
		r += absB
		q--
	}

	if b < 0 {
		q = -q
	}

	fmt.Println(q, r)
}
