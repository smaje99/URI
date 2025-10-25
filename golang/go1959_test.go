package beecrowd

import "testing"

func TestRegularSimplePolygons(t *testing.T) {
	// Define test cases
	tests := []struct {
		input    string
		expected string
	}{
		{"3 10", "30\n"},
		{"4 5", "20\n"},
		{"1000000 4000", "4000000000\n"},
		{"3 1", "3\n"},
		{"9 8", "72\n"},
		{"1000000 1000", "1000000000\n"},
	}

	// Iterate over the test cases
	for _, tt := range tests {
		RunTest(t, RegularSimplePolygons, tt.input, tt.expected)
	}
}
