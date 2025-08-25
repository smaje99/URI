package beecrowd

import "testing"

func TestConvertToHexadecimal(t *testing.T) {
	// Define test cases
	tests := []struct {
		input    string
		expected string
	}{
		{"10", "A\n"},
		{"15", "F\n"},
		{"16", "10\n"},
		{"31", "1F\n"},
		{"65535", "FFFF\n"},
	}

	// Iterate over the test cases
	for _, tt := range tests {
		RunTest(t, ConvertToHexadecimal, tt.input, tt.expected)
	}
}
