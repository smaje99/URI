import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class j1003 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int i = Integer.parseInt(br.readLine()),j = Integer.parseInt(br.readLine());
        System.out.println("SOMA = " + (i + j));
    }
}
