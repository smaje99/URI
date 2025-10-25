package beecrowd

import "testing"

func TestJumpingFrog(t *testing.T) {
	// Define test cases
	tests := []struct {
		input    string
		expected string
	}{
		{"5 10\n1 3 6 9 7 2 4 5 8 3\n", "YOU WIN\n"},
		{"1 2\n2 2\n", "YOU WIN\n"},
		{"1 2\n1 3\n", "GAME OVER\n"},
	}

	// Iterate over the test cases
	for _, tt := range tests {
		RunTest(t, JumpingFrog, tt.input, tt.expected)
	}
}
