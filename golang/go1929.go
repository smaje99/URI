/*
Beecrowd exercise 1929.
Triangle.
Beginner.

https://www.urionlinejudge.com.br/judge/problems/view/1929
*/

package beecrowd

import "fmt"

func canFormTriangle(a, b, c int) bool {
	return a+b > c && a+c > b && b+c > a
}

func Triangle() {
	var a, b, c, d int
	fmt.Scan(&a, &b, &c, &d)

	if canFormTriangle(a, b, c) ||
			canFormTriangle(a, b, d) ||
			canFormTriangle(a, c, d) ||
			canFormTriangle(b, c, d) {
		fmt.Println("S")
	} else {
		fmt.Println("N")
	}
}
