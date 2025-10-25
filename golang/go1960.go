/*
Beecrowd exercise 1960.
Roman Numerals for Page Numbers.
Beginner.
Ad-Hoc, Digits, Switch-Case.

https://www.urionlinejudge.com.br/judge/problems/view/1960
*/

package beecrowd

import "fmt"

func RomanNumeralsForPageNumbers() {
	var number int
	fmt.Scan(&number)

	// Definition of Roman numeral symbols and their Arabic equivalents
	romanMap := map[int]string{
		1000: "M",
		900:  "CM",
		500:  "D",
		400:  "CD",
		100:  "C",
		90:   "XC",
		50:   "L",
		40:   "XL",
		10:   "X",
		9:    "IX",
		5:    "V",
		4:    "IV",
		1:    "I",
	}

	// Convert the number to Roman numerals
	roman := ""
	for value, symbol := range romanMap {
		for number >= value {  // While the number is greater than or equal to the value
			number -= value
			roman += symbol
		}
	}

	fmt.Println(roman)
}
