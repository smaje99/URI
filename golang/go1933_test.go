package beecrowd

import "testing"

func TestTriDu(t *testing.T) {
	// Define test cases
	tests := []struct {
		input    string
		expected string
	}{
		{"1 2", "2\n"},
		{"3 3", "3\n"},
		{"5 4", "5\n"},
		{"10 20", "20\n"},
	}

	// Iterate over the test cases
	for _, tt := range tests {
		RunTest(t, TriDu, tt.input, tt.expected)
	}
}