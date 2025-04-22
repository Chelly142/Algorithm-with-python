import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int r, c, k;
    static int[][] A = new int[3][3];

    static class Counter implements Comparable<Counter> {
        int num, cnt;

        public Counter(int num, int cnt) {
            this.num = num;
            this.cnt = cnt;
        }

        @Override
        public int compareTo(Counter o) {
            if (this.cnt == o.cnt) return this.num - o.num;
            return this.cnt - o.cnt;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        r = Integer.parseInt(st.nextToken()) - 1;
        c = Integer.parseInt(st.nextToken()) - 1;
        k = Integer.parseInt(st.nextToken());

        for (int i = 0; i < 3; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 3; j++) {
                A[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int time = 0;
        while (time <= 100) {
            if (r < A.length && c < A[0].length && A[r][c] == k) {
                System.out.println(time);
                return;
            }

            if (A.length >= A[0].length) {
                rCalc();
            } else {
                cCalc();
            }
            time++;
        }

        System.out.println(-1);
    }

    private static void rCalc() {
        int maxCol = 0;
        int rowCount = A.length;
        int colCount = A[0].length;
        int[][] newA = new int[101][101];

        for (int i = 0; i < rowCount; i++) {
            Map<Integer, Integer> map = new HashMap<>();
            for (int j = 0; j < colCount; j++) {
                int num = A[i][j];
                if (num == 0) continue;
                map.put(num, map.getOrDefault(num, 0) + 1);
            }

            PriorityQueue<Counter> pq = new PriorityQueue<>();
            for (int num : map.keySet()) {
                pq.offer(new Counter(num, map.get(num)));
            }

            int idx = 0;
            while (!pq.isEmpty() && idx < 100) {
                Counter cnt = pq.poll();
                newA[i][idx++] = cnt.num;
                if (idx < 100) newA[i][idx++] = cnt.cnt;
            }
            maxCol = Math.max(maxCol, idx);
        }

        // 새로운 A 배열 생성
        int[][] resized = new int[rowCount][maxCol];
        for (int i = 0; i < rowCount; i++) {
            for (int j = 0; j < maxCol; j++) {
                resized[i][j] = newA[i][j];
            }
        }
        A = resized;
    }

    private static void cCalc() {
        int maxRow = 0;
        int rowCount = A.length;
        int colCount = A[0].length;
        int[][] newA = new int[101][101];

        for (int j = 0; j < colCount; j++) {
            Map<Integer, Integer> map = new HashMap<>();
            for (int i = 0; i < rowCount; i++) {
                int num = A[i][j];
                if (num == 0) continue;
                map.put(num, map.getOrDefault(num, 0) + 1);
            }

            PriorityQueue<Counter> pq = new PriorityQueue<>();
            for (int num : map.keySet()) {
                pq.offer(new Counter(num, map.get(num)));
            }

            int idx = 0;
            while (!pq.isEmpty() && idx < 100) {
                Counter cnt = pq.poll();
                newA[idx++][j] = cnt.num;
                if (idx < 100) newA[idx++][j] = cnt.cnt;
            }
            maxRow = Math.max(maxRow, idx);
        }

        // 새로운 A 배열 생성
        int[][] resized = new int[maxRow][colCount];
        for (int i = 0; i < maxRow; i++) {
            for (int j = 0; j < colCount; j++) {
                resized[i][j] = newA[i][j];
            }
        }
        A = resized;
    }
}
