import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());

        int[] weights = new int[n + 1];
        st = new StringTokenizer(br.readLine());
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            weights[i] = Integer.parseInt(st.nextToken());
            sum += weights[i];
        }

        int k = Integer.parseInt(br.readLine());
        int[] check = new int[k];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < k; i++) {
            check[i] = Integer.parseInt(st.nextToken());
        }

        int[][] dp = new int[n+1][sum + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= sum; j++) {
                if(j==weights[i]){
                    dp[i][j] =j;
                }
                else if (j - weights[i] >= 0 && dp[i - 1][j - weights[i]] + weights[i] == j) {
                    dp[i][j] = j;
                }
                else if (weights[i] - j >= 0 && weights[i] - dp[i - 1][weights[i] - j] == j) {
                    dp[i][j] = j;
                }
                else if (weights[i] + j <= sum && dp[i - 1][weights[i] + j] - weights[i] == j) {
                    dp[i][j] = j;
                }
                else{
                    dp[i][j] = dp[i-1][j];
                }
            }
//            System.out.println(Arrays.toString(dp[i]));
        }
//        if (weights[i] > j) {
//            if (weights[i] - dp[weights[i] - j] == j) {
//                dp[j] = j;
//            }
//        } else if (weights[i] + j <= sum) {
//            if (dp[weights[i] + j] - weights[i] == j) {
//                dp[j] = j;
//            }
//        } else {
//            dp[j] = Math.max(dp[j], dp[j - weights[i]] + weights[i]);
//        }

        for (int c : check) {
            if (c > sum) {
                System.out.print("N ");
                continue;
            }
            if (dp[n][c] == c) {
                System.out.print("Y ");
            } else {
                System.out.print("N ");
            }
        }
    }

}
