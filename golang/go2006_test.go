package beecrowd

import (
	"testing"
)

/*
TestIdentifyingTea tests the implementation of the Beecrowd exercise 1858.
It runs a series of inputs and checks if the output is as expected.
*/
func TestIdentifyingTea(t *testing.T) {
	// Define test cases
	tests := []struct {
		input 		string
		expected 	string
	}{
		{
			input: "1\n1 2 3 2 1\n",
			expected: "2\n",
		},
		{
			input: "3\n4 1 1 2 1\n",
			expected: "0\n",
		},
		{
			input: "2\n2 4 3 1 2\n",
			expected: "2\n",
		},
	}

	// Iterate over the test cases
	for _, test := range tests {
		RunTest(t, IdentifyingTea, test.input, test.expected)
	}
}
