import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
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

        boolean[][] dp = new boolean[n + 1][sum + 1]; // dp[i][j]: i개의 추로 j 무게를 만들 수 있는가?
        dp[0][0] = true; // 초기값 설정

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= sum; j++) {
                if (!dp[i - 1][j]) {
                    continue;// 이전 상태에서 j 무게를 만들 수 있으면
                }
                dp[i][j] = true; // 그대로 유지
                if (j + weights[i] <= sum) dp[i][j + weights[i]] = true; // 현재 추를 더한 경우
                dp[i][Math.abs(j - weights[i])] = true; // 현재 추를 뺀 경우

            }
        }

        for (int c : check) {
            if (c > sum) {
                sb.append("N ");
            } else if (dp[n][c]) {
                sb.append("Y ");
            } else {
                sb.append("N ");
            }
        }

        System.out.println(sb); // 결과 출력
    }
}
