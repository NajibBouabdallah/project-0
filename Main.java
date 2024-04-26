import java.util.*;

public class Main {
    
public static int max(int a, int b)
{
    return a > b ? a : b;
}

    public static char[][] Thang(char X)
    {
        String Dic = "ABCDEFGHIJKLMNOPQRSTUVWXZ";
        char[][] Box = new char[Dic.indexOf(X) * 2 + 1][Dic.indexOf(X) * 2 + 1];
        int center = Dic.indexOf(X + 1);
        for(int i = 0; i <= Dic.indexOf(X)*2 ; i++)
        {
            for(int j = 0; j <= Dic.indexOf(X)*2; j++)
            {
                int distance = max(Math.abs(Dic.indexOf(X) - i), Math.abs(Dic.indexOf(X) - j));
                Box[i][j] = Dic.charAt(distance);
            }
        }
        return Box;
    }
    public static void main(String[] args) 
    {
        String Dic = "ABCDEFGHIJKLMNOPQRSTUVWXZ";
        char X = 'Z';
        char[][] result = Thang(X);

        for(int i = 0; i <= Dic.indexOf(X) * 2; i++)
        {
            for(int j = 0; j <= Dic.indexOf(X) * 2; j++)
            {
                System.out.print(result[i][j]);
            }
            System.out.println();
        }
    }
}
