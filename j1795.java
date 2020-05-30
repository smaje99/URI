import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
public class p1795 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter writer = new PrintWriter(System.out);
        int i = Integer.parseInt(br.readLine());
        long ans = 1;
        while ((i--) > 0) ans *= 3;
        System.out.println(ans);
    }
}