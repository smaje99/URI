package beecrowd

import (
	"bytes"
	"io"
	"os"
	"testing"
)

/*
Helper function to simulate the input/output process for a Beecrowd-like environment.
It uses a byte buffer to capture the output and compares it against the expected result.

Parameters:
- input: string representing the input data (formatted as it would be entered).
- expected: string representing the expected output (formatted as it would be printed).
*/
func testColumnInArray(t *testing.T, input, expected string) {
	// Redirect the standard output to a buffer to capture printed results
	originalStdout := os.Stdout
	var buf bytes.Buffer
	r, w, _ := os.Pipe()
	os.Stdout = w

	// Simulate standard input by manually scanning inputs
	originalStdin := os.Stdin
	pr, pw, _ := os.Pipe()
	os.Stdin = pr
	pw.Write([]byte(input))
	pw.Close()

	// Call the ColumnInArray function (main function)
	ColumnInArray()

	// Restore the original standard output and input
	w.Close()
	os.Stdout = originalStdout
	io.Copy(&buf, r)
	os.Stdin = originalStdin

	// Compare the captured output with the expected output
	if buf.String() != expected {
		t.Errorf(
			"For input\n%s\nexpected output:\n%s\nbut got:\n%s",
			input,
			expected,
			buf.String(),
		)
	}
}

/*
TestArraySelectionI tests the implementation of the Beecrowd exercise 1174.
It runs a series of inputs and checks if the output is as expected.
*/
func TestColumnInArray(t *testing.T) {
	// Define test cases
	tests := []struct {
		input    string
		expected string
	}{
		{
			input: `1
S
23
-8
-93
46
84
-94
-56
-88
20
-15
-8
44
-38
-88
-63
-96
-30
82
70
-10
1
-6
-16
-8
-38
-40
-99
83
19
66
-47
-9
71
17
-21
59
-16
35
49
92
-70
39
10
41
67
-60
92
-31
45
13
-86
-87
91
29
-3
4
-19
27
29
60
14
-29
33
91
97
-67
73
94
86
41
-44
79
13
5
60
7
64
-98
34
-24
11
-2
-36
-1
-75
24
-51
88
-79
93
-6
-38
-48
34
-27
15
-68
91
2
-87
-7
-90
76
-66
47
92
-52
-22
10
-21
-29
68
-17
-26
-76
-92
-5
91
98
19
60
91
-20
80
80
-93
73
98
-30
-69
93
-73
-2
-67
52
36
-38
-64
70
28
2
-72
53
-67
`,
			expected: "6.0\n",
		},
		{
			input: `1
M
23
-8
-93
46
84
-94
-56
-88
20
-15
-8
44
-38
-88
-63
-96
-30
82
70
-10
1
-6
-16
-8
-38
-40
-99
83
19
66
-47
-9
71
17
-21
59
-16
35
49
92
-70
39
10
41
67
-60
92
-31
45
13
-86
-87
91
29
-3
4
-19
27
29
60
14
-29
33
91
97
-67
73
94
86
41
-44
79
13
5
60
7
64
-98
34
-24
11
-2
-36
-1
-75
24
-51
88
-79
93
-6
-38
-48
34
-27
15
-68
91
2
-87
-7
-90
76
-66
47
92
-52
-22
10
-21
-29
68
-17
-26
-76
-92
-5
91
98
19
60
91
-20
80
80
-93
73
98
-30
-69
93
-73
-2
-67
52
36
-38
-64
70
28
2
-72
53
-67
`,
			expected: "0.5\n",
		},
	}

	// Iterate over the test cases
	for _, test := range tests {
		testColumnInArray(t, test.input, test.expected)
	}
}
