package beecrowd

import "testing"

func TestRomanNumeralsForPageNumbers(t *testing.T) {
	// Define test cases
	tests := []struct {
		input    string
		expected string
	}{
		{"666", "DCLXVI\n"},
		{"1987", "MCMLXXXVII\n"},
		{"3999", "MMMCMXCIX\n"},
		{"44", "XLIV\n"},
		{"2024", "MMXXIV\n"},
		{"1", "I\n"},
	}

	// Iterate over the test cases
	for _, tt := range tests {
		RunTest(t, RomanNumeralsForPageNumbers, tt.input, tt.expected)
	}
}
