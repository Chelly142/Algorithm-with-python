import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 빠른 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        // 입력 받을 리스트
        List<int[]> lines = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            lines.add(new int[]{start, end});
        }

        // 시작점을 기준으로 정렬
        lines.sort(Comparator.comparingInt(a -> a[0]));

        int answer = 0;
        int s = lines.get(0)[0];
        int e = lines.get(0)[1];

        for (int i = 1; i < n; i++) {
            int curStart = lines.get(i)[0];
            int curEnd = lines.get(i)[1];

            if (e >= curStart) {
                e = Math.max(e, curEnd);
            } else {
                answer += e - s;
                s = curStart;
                e = curEnd;
            }
        }
        answer += e - s;

        System.out.println(answer);
    }
}
