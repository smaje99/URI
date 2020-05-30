import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;

public class j1002 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        double d = Double.parseDouble(br.readLine());
        DecimalFormatSymbols symbols = new DecimalFormatSymbols();
        symbols.setDecimalSeparator('.');
        System.out.println("A=" + new DecimalFormat("###########################.0000",symbols).format(3.14159 * Math.pow(d,2)));
    }
}