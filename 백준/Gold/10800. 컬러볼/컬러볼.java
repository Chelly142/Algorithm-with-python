import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    static class Ball {
        int idx;
        int color;
        int weight;

        public Ball(int idx, int color, int weight) {
            this.idx = idx;
            this.color = color;
            this.weight = weight;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());

        Ball[] balls = new Ball[n];  // 0번 인덱스 필요 없음
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            balls[i] = new Ball(i, Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }

        // 공을 무게 기준으로 오름차순 정렬
        Arrays.sort(balls, Comparator.comparingInt(c -> c.weight));

        int totalSum = 0;
        HashMap<Integer, Integer> colorSum = new HashMap<>();
        int[] answer = new int[n];
        int j = 0;  // 같은 무게를 가진 공들의 시작 위치

        for (int i = 0; i < n; i++) {
            Ball ball = balls[i];

            // 이전 공들과 무게가 다르면 갱신
            while (j < i && balls[j].weight < ball.weight) {
                totalSum += balls[j].weight;
                colorSum.put(balls[j].color, colorSum.getOrDefault(balls[j].color, 0) + balls[j].weight);
                j++;
            }

            // 현재 공의 결과 계산
            answer[ball.idx] = totalSum - colorSum.getOrDefault(ball.color, 0);
        }

        // 결과 출력 (입력된 순서대로)
        for (int i = 0; i < n; i++) {
            System.out.println(answer[i]);
        }
    }
}
