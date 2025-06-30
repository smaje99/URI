/*
Beecrowd exercise 1176.
Arreglo de Fibonacci.
Beginner.
Array.

https://www.urionlinejudge.com.br/judge/problems/view/1176
*/

package beecrowd

import "fmt"

func FibonacciArray() {
	var N int
	fmt.Scan(&N)

	fib := make([]int, 61)
	fib[0], fib[1] = 0, 1

	for i := 2; i <= 60; i++ {
		fib[i] = fib[i-1] + fib[i-2]
	}

	for range N {
		var X int
		fmt.Scan(&X)
		fmt.Printf("Fib(%d) = %d\n", X, fib[X])
	}
}

