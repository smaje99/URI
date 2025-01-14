package beecrowd

import (
	"testing"
)

/*
TestDancingSentence tests the implementation of the Beecrowd exercise 1858.
It runs a series of inputs and checks if the output is as expected.
*/
func TestDancingSentence(t *testing.T) {
	// Define test cases
	tests := []struct {
		input 		string
		expected 	string
	}{
		{
			input: `ma na mmmmmmmmmm         
tthuuhjnjnYTTGUEGFUhggu567Y
`,
			expected: `Ma Na MmMmMmMmMm         
TtHuUhJnJnYtTgUeGfUhGgU567y
`,
		},
		{
			input: `This is a dancing sentence
  This   is         a  dancing   sentence  
aaaaaaaaaaa
z
`,
			expected: `ThIs Is A dAnCiNg SeNtEnCe
  ThIs   Is         A  dAnCiNg   SeNtEnCe  
AaAaAaAaAaA
Z
`,
		},
	}

	// Iterate over the test cases
	for _, test := range tests {
		RunTest(t, DancingSentence, test.input, test.expected)
	}
}
