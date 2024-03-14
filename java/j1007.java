import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class j1007 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int A = Integer.parseInt(br.readLine()), B = Integer.parseInt(br.readLine()),C = Integer.parseInt(br.readLine()),D = Integer.parseInt(br.readLine());
        System.out.println("DIFERENCA = " + (A * B - C * D));
    }
}
