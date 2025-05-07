import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n, m;
    static ArrayList<Node>[] graph;
    static int[] siya;

    static class Node implements Comparable<Node> {
        int to;
        long cost;

        public Node(int to, long cost) {
            this.to = to;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node o) {
            return Long.compare(this.cost, o.cost);
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();

        siya = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            siya[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            if ((siya[a] == 0 && siya[b] == 0) || a == n - 1 || b == n - 1) {
                graph[a].add(new Node(b, c));
                graph[b].add(new Node(a, c));
            }
        }

        long answer = dijkstra();
        if (answer == Long.MAX_VALUE) System.out.println(-1);
        else System.out.println(answer);
    }

    private static long dijkstra() {
        long[] dist = new long[n];
        Arrays.fill(dist, Long.MAX_VALUE);
        dist[0] = 0;

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(0, 0));

        while (!pq.isEmpty()) {
            Node now = pq.poll();

            if (dist[now.to] < now.cost) continue;

            for (Node nxt : graph[now.to]) {
                if (dist[nxt.to] > dist[now.to] + nxt.cost) {
                    dist[nxt.to] = dist[now.to] + nxt.cost;
                    pq.add(new Node(nxt.to, dist[nxt.to]));  // 누적된 비용 사용!
                }
            }
        }

        return dist[n - 1];
    }
}
