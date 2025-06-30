package beecrowd

import "testing"

/*
TestFibonacciArray tests the implementation of the Beecrowd exercise 1176.
It runs a series of inputs and checks if the output is as expected.
*/
func TestFibonacciArray(t *testing.T) {
	// Define test cases
	tests := []struct {
		input    string
		expected string
	}{
		{
			input:    "3\n0\n1\n2\n",
			expected: "Fib(0) = 0\nFib(1) = 1\nFib(2) = 1\n",
		},
		{
			input:    "5\n3\n4\n5\n6\n7\n",
			expected: "Fib(3) = 2\nFib(4) = 3\nFib(5) = 5\nFib(6) = 8\nFib(7) = 13\n",
		},
		{
			input:    "1\n60\n",
			expected: "Fib(60) = 1548008755920\n",
		},
	}

	// Iterate over the test cases
	for _, test := range tests {
		RunTest(t, FibonacciArray, test.input, test.expected)
	}
}
