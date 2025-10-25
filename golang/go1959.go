/*
Beecrowd exercise 1959.
Regular Simple Polygons.
Beginner.
Ad-Hoc, Overflow.

https://www.urionlinejudge.com.br/judge/problems/view/1959
*/

package beecrowd

import "fmt"

func RegularSimplePolygons() {
	var numberOfSides, lengthOfEachSide int
	fmt.Scan(&numberOfSides, &lengthOfEachSide)

	if numberOfSides >= 3 && numberOfSides <= 1_000_000  && lengthOfEachSide >= 1 && lengthOfEachSide <= 4000 {
		fmt.Println(numberOfSides * lengthOfEachSide)
	}
}
