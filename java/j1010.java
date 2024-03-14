import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;

public class j1010 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String n = br.readLine(), n1 = br.readLine();
        String[] ns = .split(" "), n1s = n1.split(" ");
        DecimalFormatSymbols symbols = new DecimalFormatSymbols();
        symbols.setDecimalSeparator('.');
        System.out.println("VALOR A PAGAR: R$ " + new DecimalFormat("#####################.00", symbols).format(((Integer.parseInt(ns[1]) * Double.parseDouble(ns[2])) + (Integer.parseInt(n1s[1]) * Double.parseDouble(n1s[2])))));
    }
}
