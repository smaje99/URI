/*
Beecrowd exercise 1234.
Dancing Sentence.
String
https://www.urionlinejudge.com.br/judge/problems/view/1234
*/

package beecrowd

import (
	"bufio"
	"fmt"
	"os"
	"unicode"
)

func DancingSentence() {
	scanner := bufio.NewScanner(os.Stdin)  // Create a scanner to read from standard input

	for scanner.Scan() {
		line := scanner.Text()
		upper := true
		result := []rune(line)  // Convert string to rune slice (array)

		for i, c := range result {
			if unicode.IsLetter(c) {
				if upper {
					result[i] = unicode.ToUpper(c)
				} else {
					result[i] = unicode.ToLower(c)
				}
				upper = !upper
			}
		}

		fmt.Println(string(result))
	}
}
