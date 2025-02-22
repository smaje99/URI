package beecrowd

import (
	"testing"
)

/*
TestTheonsAnswer tests the implementation of the Beecrowd exercise 1858.
It runs a series of inputs and checks if the output is as expected.
*/
func TestTheonsAnswer(t *testing.T) {
	// Define test cases
	tests := []struct {
		input 		string
		expected 	string
	}{
		{
			input: `100
12 17 3 18 2 1 4 14 0 8 12 16 9 4 18 2 16 13 15 16 17 6 15 14 0 1 12 5 1 12 1 2 7 13 2 5 0 7 6 7 10 1 4 5 3 12 0 19 11 14 18 17 17 18 10 4 4 12 6 17 16 19 2 13 19 1 6 2 15 2 3 3 0 10 17 15 17 10 18 6 7 15 10 15 5 2 17 13 14 9 4 15 6 3 19 6 2 2 13 15
`,
			expected: `9
`,
		},
		{
			input: `70
20 18 19 17 20 2 6 8 8 2 12 6 14 7 10 9 3 18 2 3 17 16 4 4 4 3 19 1 19 13 18 18 15 8 11 9 6 8 11 3 14 3 10 1 19 14 4 1 19 14 13 11 17 6 14 19 6 5 10 9 1 0 12 11 2 17 10 4 2 7 3
`,
			expected: `62
`,
		},
	}

	// Iterate over the test cases
	for _, test := range tests {
		RunTest(t, TheonsAnswer, test.input, test.expected)
	}
}
