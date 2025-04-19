import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Map.Entry;
import java.util.StringTokenizer;

import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        int[] a = new int[n];
        int[] b = new int[n];
        int[] c = new int[n];
        int[] d = new int[n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            a[i] = Integer.parseInt(st.nextToken());
            b[i] = Integer.parseInt(st.nextToken());
            c[i] = Integer.parseInt(st.nextToken());
            d[i] = Integer.parseInt(st.nextToken());
        }
        int[] left = new int[n * n];
        int[] right = new int[n * n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                left[i * n + j] = a[i] + b[j];
                right[i * n + j] = c[i] + d[j];
            }
        }
        Arrays.sort(left);
        Arrays.sort(right);

        long answer = 0;
        int start = 0;
        int end = n * n - 1;

        while (start < n * n && end >= 0) {
            if (left[start] + right[end] == 0) {
                int nxti = start;
                int nxtj = end;
                long leftCnt = 0;
                long rightCnt = 0;
                while (nxti < n * n && left[nxti] == left[start]) {
                    nxti++;
                    leftCnt++;
                }
                while ( nxtj >= 0 && right[nxtj] == right[end]) {
                    nxtj--;
                    rightCnt++;
                }
                answer += (leftCnt * rightCnt);
                start = nxti;
                end = nxtj;
            } else if (left[start] + right[end] > 0) {
                end--;
            } else if (left[start] + right[end] < 0) {
                start++;
            }
        }

        System.out.println(answer);
    }
}