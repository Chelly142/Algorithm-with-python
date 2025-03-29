import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 빠른 입력 처리
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // 입력 받기
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        // 우선순위 큐 사용 (작은 값이 먼저 나오도록)
        PriorityQueue<Long> pq = new PriorityQueue<>();

        // 숫자들 입력
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            pq.add(Long.parseLong(st.nextToken()));
        }

        // m번 반복
        for (int i = 0; i < m; i++) {
            long first = pq.poll();
            long second = pq.poll();
            long sum = first + second;

            pq.add(sum);
            pq.add(sum);
        }

        // 전체 합 계산
        long result = 0;
        while (!pq.isEmpty()) {
            result += pq.poll();
        }

        System.out.println(result);
    }
}
