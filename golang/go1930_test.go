package beecrowd

import (
	"testing"
)

/*
TestElectricalOutlet tests the implementation of the Beecrowd exercise 1858.
It runs a series of inputs and checks if the output is as expected.
*/
func TestElectricalOutlet(t *testing.T) {
	// Define test cases
	tests := []struct {
		input 		string
		expected 	string
	}{
		{
			input: "2 4 3 2\n",
			expected: "8\n",
		},
		{
			input: "6 6 6 6\n",
			expected: "21\n",
		},
		{
			input: "2 2 2 2\n",
			expected: "5\n",
		},
	}

	// Iterate over the test cases
	for _, test := range tests {
		RunTest(t, ElectricalOutlet, test.input, test.expected)
	}
}
