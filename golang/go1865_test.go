package beecrowd

import "testing"

/*
TestMjolnir tests the implementation of the Beecrowd exercise 1865.
It runs a series of inputs and checks if the output is as expected.
*/
func TestMjolnir(t *testing.T) {
	// Define test cases
	tests := []struct {
		input    string
		expected string
	}{
		{
			input:    "3\nThor 5000\nHulk 3000\nIronMan 4000\n",
			expected: "Y\nN\nN\n",
		},
		{
			input:    "2\nThor 1000\nLoki 2000\n",
			expected: "Y\nN\n",
		},
	}

	// Iterate over the test cases
	for _, test := range tests {
		RunTest(t, Mjolnir, test.input, test.expected)
	}
}
