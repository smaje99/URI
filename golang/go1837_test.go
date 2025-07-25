package beecrowd

import "testing"

func TestPreface(t *testing.T) {
	// Define test cases
	tests := []struct {
		input    string
		expected string
	}{
		{"7 3", "2 1\n"},
		{"-7 3", "-3 2\n"},
		{"7 -3", "-2 1\n"},
		{"-7 -3", "3 2\n"},
		{"-62 -59", "2 56\n"},
	}

	// Iterate over the test cases
	for _, tt := range tests {
		RunTest(t, Preface, tt.input, tt.expected)
	}
}
