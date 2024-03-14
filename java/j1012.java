import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;
import java.util.StringTokenizer;

public class j1012 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter writer = new PrintWriter(System.out);
        StringTokenizer tokenizer = new StringTokenizer(br.readLine());
        float a = Float.parseFloat(tokenizer.nextToken()), b = Float.parseFloat(tokenizer.nextToken()), c = Float.parseFloat(tokenizer.nextToken());
        writer.println("TRIANGULO: " + decimal((a * c) / 2));
        writer.println("CIRCULO: " + decimal((float) (Math.pow(c, 2) * 3.14159)));
        writer.println("TRAPEZIO: " + decimal(((a + b) / 2) * c));
        writer.println("QUADRADO: " + decimal((float) Math.pow(b, 2)));
        writer.println("RETANGULO: " + decimal(a * b));
        writer.close();
    }

    private static String decimal(float n) {
        DecimalFormatSymbols symbols = new DecimalFormatSymbols();
        symbols.setDecimalSeparator('.');
        return new DecimalFormat("##################.000", symbols).format(n);
    }
}
