import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	
	static class Node implements Comparable<Node>{
		int to;
		int weight;
		
		public Node(int to, int weight) {
			this.to = to;
			this.weight = weight;
		}

		@Override
		public int compareTo(Node node) {
			return this.weight - node.weight;
		}
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int r = Integer.parseInt(st.nextToken());
		
		
		st = new StringTokenizer(br.readLine());
		
		int[] item = new int[n+1];
		List<List<Node>> graph = new ArrayList<>();
		graph.add(new ArrayList<Node>());

		for(int i = 1; i<=n;i++) {
			item[i] = Integer.parseInt(st.nextToken());
			graph.add(new ArrayList<Node>());
		}
		
		for(int i = 0; i<r;i++) {
			st = new StringTokenizer(br.readLine());
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
			int weight = Integer.parseInt(st.nextToken());
			
			graph.get(from).add(new Node(to,weight));
			graph.get(to).add(new Node(from,weight));	
		}
		
		// 한 정점에 대한 다른 모든 정점의 최단 거리 구하고 배열 d
		// 다른 정점들(b)까지 거리 중 m 보다 짧은 경우 해당 다른 노드(b)의 item[b]를 더헤
		// 다 더한 값이 최대가 되는 시작 지점을 구하면 끝
		
		
		int INF = (int)1e9;
		int answer =0;
		for(int start = 1; start<=n;start++) {
			int[] d = new int[n+1];
			Arrays.fill(d, INF);
			PriorityQueue<Node> pq = new PriorityQueue<>();
			boolean[] visited = new boolean[n+1];
			d[start] = 0;
			visited[start] = true;
			pq.add(new Node(start,0));
			
			while(!pq.isEmpty()) {
				Node now = pq.poll();
				int nowNodeNum = now.to;
				
				List<Node> nxtNodes = graph.get(nowNodeNum);
				for(Node nxt : nxtNodes) {
					if(d[nxt.to]>d[now.to]+nxt.weight) {
						pq.add(nxt);
						d[nxt.to] = d[now.to]+nxt.weight;
					}
				}
			}
			
			int sum = 0;
			for(int i= 1; i<=n;i++) {
				if(d[i]<=m) {
					sum+=item[i];
				}
			}
			answer = Math.max(answer, sum);
		}
		System.out.println(answer);
		
		
		
		
	}

}
