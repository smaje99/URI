/*
Beecrowd exercise 1531.
Fibonacci Again!.
Mathematics.
Linear Recurrences.

See: https://judge.beecrowd.com/es/problems/view/1531
*/

package beecrowd

import (
	"bufio"
	"os"
)

const (
	preLim = 70
)

var (
	preCompFib [preLim + 1]int64
	pisano     = make(map[int64]int64)
)

func init() {
	preCompFib[0], preCompFib[1] = 0, 1
	for i := 2; i <= preLim; i++ {
		preCompFib[i] = preCompFib[i-1] + preCompFib[i-2]
	}
}

func FibonacciAgain() {
	in := bufio.NewReaderSize(os.Stdin, 1<<20)
	out := bufio.NewWriterSize(os.Stdout, 1<<20)
	defer out.Flush()

	for {
		N, ok := readInt64(in)
		if !ok {
			break
		}
		M, _ := readInt64(in)

		if M == 1 {
			out.WriteByte('0')
			out.WriteByte('\n')
			continue
		}

		piM := getPisanoPeriod(M)
		fibNModPi := fastFibMod(N, piM)
		ans := fastFibMod(fibNModPi, M)

		out.WriteString(int64ToString(ans))
		out.WriteByte('\n')
	}
}

// fastFibMod calcula Fib(n) % mod usando:
// - tabla pre-computada para n <= 70
// - fast doubling para n > 70
func fastFibMod(n, mod int64) int64 {
	if n <= preLim {
		return preCompFib[n] % mod
	}
	f, _ := fibDoublingMod(n, mod)
	return f
}

// fibDoublingMod devuelve (F(n), F(n+1)) % mod
func fibDoublingMod(n, mod int64) (int64, int64) {
	if n == 0 {
		return 0, 1
	}
	a, b := fibDoublingMod(n>>1, mod) // a = F(k), b = F(k+1)
	// c = F(2k)
	// d = F(2k+1)
	// c = F(k) * [2*F(k+1) - F(k)]
	// d = F(k)^2 + F(k+1)^2
	t := (2*b - a) % mod
	if t < 0 {
		t += mod
	}
	c := (a * t) % mod
	d := (a*a%mod + b*b%mod) % mod
	if n&1 == 0 {
		return c, d
	}
	return d, (c + d) % mod
}

func getPisanoPeriod(m int64) int64 {
	if v, ok := pisano[m]; ok {
		return v
	}
	var prev, curr int64 = 0, 1
	for i := int64(0); i < m*6; i++ {
		prev, curr = curr, (prev+curr)%m
		if prev == 0 && curr == 1 {
			pisano[m] = i + 1
			return i + 1
		}
	}
	return -1
}

// -------------------- Fast IO helpers --------------------

func readInt64(r *bufio.Reader) (int64, bool) {
	var sign int64 = 1
	var val int64 = 0

	// skip non-digit
	b, err := r.ReadByte()
	for err == nil && (b < '0' || b > '9') && b != '-' {
		b, err = r.ReadByte()
	}
	if err != nil {
		return 0, false
	}

	if b == '-' {
		sign = -1
		b, err = r.ReadByte()
		if err != nil {
			return 0, false
		}
	}

	for b >= '0' && b <= '9' {
		val = val*10 + int64(b-'0')
		b, err = r.ReadByte()
		if err != nil {
			break
		}
	}
	return sign * val, true
}

func int64ToString(x int64) string {
	var buf [32]byte
	b := buf[:0]
	return string(strconvAppendInt(b, x))
}

func strconvAppendInt(dst []byte, i int64) []byte {
	// más rápido que fmt.Sprintf para nuestro caso
	return appendInt(dst, i)
}

// Versión simple basada en bytes, suficiente aquí
func appendInt(dst []byte, i int64) []byte {
	if i == 0 {
		return append(dst, '0')
	}
	neg := i < 0
	if neg {
		i = -i
	}
	var buf [20]byte
	pos := len(buf)
	for i > 0 {
		pos--
		buf[pos] = byte('0' + i%10)
		i /= 10
	}
	if neg {
		pos--
		buf[pos] = '-'
	}
	return append(dst, buf[pos:]...)
}
