import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	static char[][] graph = new char[5][5];
	static int[] dr = { 0, 0, 1, -1 };
	static int[] dc = { -1, 1, 0, 0 };
	static int answer = 0;
	static boolean[][] visited = new boolean[5][5];

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		for (int i = 0; i < 5; i++) {
			String line = br.readLine();
			for (int j = 0; j < 5; j++) {
				graph[i][j] = line.charAt(j);
			}
		}
//		for (int t = 4; t <= 7; t++) {
//			visited = new boolean[5][5];
//			for (int i = 0; i < 5; i++) {
//				for (int j = 0; j < 5; j++) {
//					visited[i][j] = true;
//					boolean[][] v = new boolean[5][5];
//					back(t, i, j, 0, 0, v);
//				}
//			}
//		}
		for (int bitmask = 0; bitmask < (1 << 25); bitmask++) {
			if (Integer.bitCount(bitmask) == 7) {
				if (checkContinue(bitmask) && checkPricess(bitmask)) {
					answer++;
				}
			}
		}
		System.out.println(answer);
	}

	private static boolean checkPricess(int bitmask) {
		int prinCnt = 0;
		for (int i = 0; i < 25; i++) {
	        if ((bitmask & (1 << i)) != 0) {
	            if(graph[i / 5][i%5]=='S') {
	            	prinCnt++;
	            }
	        }
	    }
		return prinCnt>=4;
	}

	private static boolean checkContinue(int bitmask) {
	    int areaSize = 0;
	    boolean[][] visited = new boolean[5][5];
	    ArrayDeque<int[]> q = new ArrayDeque<>();

	    int r = -1, c = -1;
	    for (int i = 0; i < 25; i++) {
	        if ((bitmask & (1 << i)) != 0) {
	            r = i / 5;
	            c = i % 5;
	            break;
	        }
	    }

	    q.add(new int[] { r, c });
	    visited[r][c] = true;
	    areaSize++;

	    while (!q.isEmpty()) {
	        int[] cur = q.poll();
	        int cr = cur[0];
	        int cc = cur[1];

	        for (int d = 0; d < 4; d++) {
	            int nr = cr + dr[d];
	            int nc = cc + dc[d];

	            if (nr < 0 || nr >= 5 || nc < 0 || nc >= 5) continue;
	            if (visited[nr][nc]) continue;

	            int idx = nr * 5 + nc;
	            if ((bitmask & (1 << idx)) == 0) continue; 

	            visited[nr][nc] = true;
	            q.add(new int[] { nr, nc });
	            areaSize++;
	        }
	    }

	    return areaSize == 7;
	}


//	private static void back(int maxPrin, int nowR, int nowC, int size, int nowPrin, boolean[][] v) {
//		if (size == 7) {
//			if (nowPrin == maxPrin) {
//				answer++;
//			}
//			return;
//		}
//		for (int d = 0; d < 4; d++) {
//			int nxtR = nowR + dr[d];
//			int nxtC = nowC + dc[d];
//			if (isRange(nxtR, nxtC) && !v[nxtR][nxtC]) {
//				v[nxtR][nxtC] = true;
//
//				if (graph[nxtR][nxtC] == 'S') {
//					back(maxPrin, nxtR, nxtC, size + 1, nowPrin + 1, v);
//				} else {
//					back(maxPrin, nxtR, nxtC, size + 1, nowPrin, v);
//				}
//				v[nxtR][nxtC] = false;
//				
//			}
//		}
//	}

	private static boolean isRange(int r, int c) {
		return r > 5 && r >= 0 && c > 5 && c >= 0;
	}

}
