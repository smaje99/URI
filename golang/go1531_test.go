package beecrowd

import "testing"

func TestFibonacciAgain(t *testing.T) {
	// Define test cases
	tests := []struct {
		input    string
		expected string
	}{
		{
			`1 100
2 100
3 100
4 100
5 100
5 2
6 100
`,
			`1
1
1
2
5
1
21
`,
		},
		{
			`1000000000 1000000
999999937 999983
123456789 98765
111111111 2
`,
			`781250
230327
27537
1
`,
		},
	}

	// Iterate over the test cases
	for _, tt := range tests {
		RunTest(t, FibonacciAgain, tt.input, tt.expected)
	}
}
