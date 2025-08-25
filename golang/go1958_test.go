package beecrowd

import "testing"

func TestScientificNotation(t *testing.T) {
	// Define test cases
	tests := []struct {
		input    string
		expected string
	}{
		{"3.141592", "+3.1416E+00\n"},
		{"1.618033", "+1.6180E+00\n"},
		{"602214085774747474747474", "+6.0221E+23\n"},
		{"-0.000027", "-2.7000E-05\n"},
		{
			"-10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
			"-1.0000E+100\n",
		},
	}

	// Iterate over the test cases
	for _, tt := range tests {
		RunTest(t, ScientificNotation, tt.input, tt.expected)
	}
}
