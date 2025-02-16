
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Scanner;
//import java.io.FileInputStream;

// 이동하는 시간 고려 X
// S -> G 로 갈때 경로 숫자 합이 최소
// 완탐 필요?
// 지도 크기 100X100
// DP 인가?
// 간선에 비용이 있다...
// 다익스트라?
// 그렇다면 노드당 간선 정보를 저장해야 겠네?
// 간선 갯수 40000


class Solution {
    static class Node {
        int idx;
        int cost;

        // 생성자
        Node(int idx, int cost) {
            this.idx = idx;
            this.cost = cost;
        }
    }

    static final int[] dx = {-1, 1, 0, 0};
    static final int[] dy = {0, 0, -1, 1};

    static int n;
    static int[][] map;

    public static void main(String args[]) throws Exception {

//        System.setIn(new FileInputStream("src/input.txt"));
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int T;
        T = Integer.parseInt(bf.readLine());

        for (int test_case = 1; test_case <= T; test_case++) {
            n = Integer.parseInt(bf.readLine());
            map = new int[n][n];

            for (int i = 0; i < n; i++) {
                String line = bf.readLine();
                for (int j = 0; j < n; j++) {
                    map[i][j] = line.charAt(j) - '0';
                }
            }
            System.out.println("#"+test_case+" " +solve(getGraph()));
        }

    }

    private static boolean isRange(int i, int j) {
        return i >= 0 && i < n && j >= 0 && j < n;
    }

    private static ArrayList<Node>[] getGraph() {
        ArrayList<Node>[] graph = new ArrayList[n * n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                graph[n * i + j] = new ArrayList<>();
                for (int k = 0; k < 4; k++) {
                    if (isRange(i + dx[k], j + dy[k])) {
                        graph[n * i + j].add(new Node(n * (i + dx[k]) + j + dy[k], map[i + dx[k]][j + dy[k]]));
                    }
                }
            }
        }
//        System.out.println("\n");
//        for (int i = 0; i < n*n; i++) {
//            System.out.print(i+" : ");
//            for(Node node : graph[i]) {
//                System.out.print(node.idx + " ");
//            }
//            System.out.println("\n");
//        }
        return graph;
    }


    private static int solve(ArrayList<Node>[] graph) {
        int[] dist = new int[n * n];
        for (int i = 0; i < n * n; i++) {
            dist[i] = Integer.MAX_VALUE;
        }
        PriorityQueue<Node> q = new PriorityQueue<Node>((o1, o2) -> Integer.compare(o1.cost, o2.cost));
        q.offer(new Node(0, 0));

        dist[0] = 0;
        while (!q.isEmpty()) {
            Node curNode = q.poll();
            for (int i = 0; i < graph[curNode.idx].size(); i++) {
                Node nextNode = graph[curNode.idx].get(i);
                if (dist[nextNode.idx] > dist[curNode.idx] + nextNode.cost) {
                    dist[nextNode.idx] = dist[curNode.idx] + nextNode.cost;
                    q.offer(nextNode);
                }
            }
        }
//        for (int d : dist) {
//            System.out.print(d + " ");
//        }
        return dist[n*n-1];
    }
}