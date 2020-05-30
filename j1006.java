import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class j1006 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        double a = Double.parseDouble(br.readLine());
        double b = Double.parseDouble(br.readLine());
        double c = Double.parseDouble(br.readLine());
        System.out.println("MEDIA = " + (((a * 2) + (b * 3) + (c * 5)) / 10));
    }
}
