import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;

public class j1008 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine()),h=Integer.parseInt(br.readLine());
        float p = Float.parseFloat(br.readLine());
        DecimalFormatSymbols symbols = new DecimalFormatSymbols();
        symbols.setDecimalSeparator('.');
        System.out.println("NUMBER = " + n + "\nSALARY = U$ " + new DecimalFormat("##############.00", symbols).format(((float) h * p)));
    }
}