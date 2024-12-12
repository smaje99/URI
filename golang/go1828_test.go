package beecrowd

import (
	"testing"
)

/*
TestBazinga tests the implementation of the Beecrowd exercise 1828.
It runs a series of inputs and checks if the output is as expected.
*/
func TestBazinga(t *testing.T) {
	// Define test cases
	tests := []struct {
		input 		string
		expected 	string
	}{
		{
			input: `3
papel pedra
lagarto tesoura
Spock Spock
`,
			expected: `Caso #1: Bazinga!
Caso #2: Raj trapaceou!
Caso #3: De novo!
`,
		},
	}

	// Iterate over the test cases
	for _, test := range tests {
		RunTest(t, Bazinga, test.input, test.expected)
	}
}
