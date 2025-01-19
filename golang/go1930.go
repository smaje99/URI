/*
Beecrowd exercise 1930.
Electrical Outlet.
Beginner
https://www.urionlinejudge.com.br/judge/problems/view/1930
*/

package beecrowd

import (
	"fmt"
)

func ElectricalOutlet() {
	var t1, t2, t3, t4 int
	fmt.Scan(&t1, &t2, &t3, &t4)
	fmt.Println(t1 + t2 + t3 + t4 - 3)
}
