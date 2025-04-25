import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n;
    static int[] num = new int[10];
    static List<Long> candi = new ArrayList<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        for (int i = 0; i < 10; i++) {
            num[i] = i;
        }

        List<Integer> current = new ArrayList<>();
        subset(num, 0, current);

        Collections.sort(candi);

        if (n >= candi.size()) {
            System.out.println(-1);
        } else {
            System.out.println(candi.get(n));
        }
    }

    public static void subset(int[] arr, int index, List<Integer> current) {
        if (index == arr.length) {
            if (!current.isEmpty()) {
                long newNum = toNumber(current);
                candi.add(newNum);
            }
            return;
        }

        subset(arr, index + 1, current);

        current.add(arr[index]);
        subset(arr, index + 1, current);
        current.remove(current.size() - 1); 
    }

    public static long toNumber(List<Integer> digits) {
        long num = 0;
        for (int i = digits.size() - 1; i >= 0; i--) {
            num = num * 10 + digits.get(i); 
        }
        return num;
    }
}
