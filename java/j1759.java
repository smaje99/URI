import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;

public class j1759 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter writer = new PrintWriter(System.out);
        int i = Integer.parseInt(bufferedReader.readLine());
        if (i > 0 && i <= 1000000){
            while ((i--) != 0){
                if (i == 0) writer.println("Ho!");
                else writer.print("Ho ");
            }
            writer.close();
        }
    }
}
