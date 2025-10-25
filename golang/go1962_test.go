package beecrowd

import "testing"

func TestALongLongTimeAgo(t *testing.T) {
	// Define test cases
	tests := []struct {
		input    string
		expected string
	}{
		{"3\n10000\n15\n2015\n", "7986 A.C.\n2000 D.C.\n1 A.C.\n"},
		{"2\n1\n2\n", "2014 D.C.\n2013 D.C.\n"},
		{"1\n2016\n", "2 A.C.\n"},
	}

	// Iterate over the test cases
	for _, tt := range tests {
		RunTest(t, ALongLongTimeAgo, tt.input, tt.expected)
	}
}
