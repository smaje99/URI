import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;

public class j1005 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        float a = Float.parseFloat(br.readLine());
        float b = Float.parseFloat(br.readLine());
        DecimalFormatSymbols symbols = new DecimalFormatSymbols();
        symbols.setDecimalSeparator('.');
        System.out.println("MEDIA = " + new DecimalFormat("#############.00000", symbols).format(((a * 3.5)+(b * 7.5)) / 11));
    }
}