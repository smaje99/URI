package beecrowd

import (
	"testing"
)

/*
TestArraySelectionI tests the implementation of the Beecrowd exercise 1174.
It runs a series of inputs and checks if the output is as expected.
*/
func TestSquareMatrixIV(t *testing.T) {
	// Define test cases
	tests := []struct {
		input    string
		expected string
	}{
		{
			input: `5
11
`,
			expected: `20003
01110
01410
01110
30002

20000000003
02000000030
00200000300
00011111000
00011111000
00011411000
00011111000
00011111000
00300000200
03000000020
30000000002

`,
		},
		{
			input: `7
9
13
`,
			expected: `2000003
0200030
0011100
0014100
0011100
0300020
3000002

200000003
020000030
002000300
000111000
000141000
000111000
003000200
030000020
300000002

2000000000003
0200000000030
0020000000300
0002000003000
0000111110000
0000111110000
0000114110000
0000111110000
0000111110000
0003000002000
0030000000200
0300000000020
3000000000002

`,
		},
	}

	// Iterate over the test cases
	for _, test := range tests {
		RunTest(t, SquareMatrixIV, test.input, test.expected)
	}
}
