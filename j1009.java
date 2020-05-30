import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;

public class j1009 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String n = br.readLine();
        double s = Double.parseDouble(br.readLine());
        double p = Double.parseDouble(br.readLine());
        DecimalFormatSymbols symbols = new DecimalFormatSymbols();
        symbols.setDecimalSeparator('.');
        System.out.println("TOTAL = R$ " + new DecimalFormat("###############.00", symbols).format(s + (p * 0.15)));
    }
}
