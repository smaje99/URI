import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class p1114 {
    public static void main(String[] args) throws IOException {
        int n;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        do {
            n = Integer.parseInt(br.readLine());
            if (n != 2002) System.out.println("Senha Invalida");
        } while (n != 2002);
        System.out.println("Acesso Permitido");
    }
}
