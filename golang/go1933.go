/*
Beecrowd exercise 1933.
Tri-du.
Beginner.

https://www.urionlinejudge.com.br/judge/problems/view/1933
*/

package beecrowd

import "fmt"

func TriDu() {
	var A, B int
	fmt.Scan(&A, &B)

	if A == B || A > B {
		fmt.Println(A)
	} else {
		fmt.Println(B)
	}
}
