/*
Beecrowd exercise 1961.
Jumping Frog.
Beginner.
Ad-Hoc, Repetition, Absolute Difference.

https://www.urionlinejudge.com.br/judge/problems/view/1961
*/

package beecrowd

import (
	"fmt"
	"math"
)

func JumpingFrog() {
	var maxHeightJump, totalPipes int
	fmt.Scan(&maxHeightJump, &totalPipes)

	heights := make([]int, totalPipes)
	for i := 0; i < totalPipes; i++ {
		fmt.Scan(&heights[i])
	}

	win := true
	for i := range totalPipes-1 {
		diff := int(math.Abs(float64(heights[i] - heights[i+1])))
		if diff > maxHeightJump {
			win = false
			break
		}
	}

	if win {
		fmt.Println("YOU WIN")
	} else {
		fmt.Println("GAME OVER")
	}
}
