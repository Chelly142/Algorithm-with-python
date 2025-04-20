import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int n, l, r;
	static int[][] A;
	static final int[] dr = { 0, 0, 1, -1 };
	static final int[] dc = { 1, -1, 0, 0 };

	static class Point {

		int r;
		int c;
		int population;

		public Point(int r, int c, int population) {
			super();
			this.r = r;
			this.c = c;
			this.population = population;
		}

		@Override
		public String toString() {
			return "Point [r=" + r + ", c=" + c + ", population=" + population + "]";
		}

	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		l = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		A = new int[n][n];

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				A[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		boolean flag = true;
		int day = -1;
		while (flag) {
			day++;
			flag = false;
			boolean[][] visited = new boolean[n][n];

			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					if (visited[i][j])
						continue;
					ArrayDeque<Point> q = new ArrayDeque<>();
					q.add(new Point(i, j, A[i][j]));
					visited[i][j] = true;
					ArrayList<Point> united = new ArrayList<>();
					int sum = 0;
					while (!q.isEmpty()) {
						Point p = q.poll();
						united.add(p);
						sum += p.population;
						for (int d = 0; d < 4; d++) {
							int nxtR = p.r + dr[d];
							int nxtC = p.c + dc[d];

							if (isRange(nxtR, nxtC) && !visited[nxtR][nxtC] && canUnited(p.r, p.c, nxtR, nxtC)) {
								flag = true;
								visited[nxtR][nxtC] = true;
								q.add(new Point(nxtR, nxtC, A[nxtR][nxtC]));
							}

						}
					}
					int newPopulation = sum / united.size();
					for (Point p : united) {
						A[p.r][p.c] = newPopulation;
					}
				}
			}

		}
		System.out.println(day);
	}

	private static boolean canUnited(int nowR, int nowC, int nxtR, int nxtC) {
		int d = Math.abs(A[nowR][nowC] - A[nxtR][nxtC]);

		return d >= l && d <= r;
	}

	private static boolean isRange(int nxtR, int nxtC) {
		return nxtR >= 0 && nxtR < n && nxtC >= 0 && nxtC < n;
	}
}
