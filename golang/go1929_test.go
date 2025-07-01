package beecrowd

import (
	"testing"
)

func TestCanFormTriangle(t *testing.T) {
	// Define test cases
	tests := []struct {
		input    string
		expected string
	}{
		{"6 9 22 15", "S\n"},
		{"14 40 12 60", "N\n"},
		{"86 23 39 21", "S\n"},
		{"26 91 49 36", "S\n"},
	}

	for _, tt := range tests {
		RunTest(t, Triangle, tt.input, tt.expected)
	}
}
