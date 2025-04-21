import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int R, C, T;
	static int[][] map;
	static int[] air; // 공기청정기 위치 (위, 아래)

	static final int[] dr = { -1, 1, 0, 0 };
	static final int[] dc = { 0, 0, -1, 1 };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		st = new StringTokenizer(br.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		T = Integer.parseInt(st.nextToken());

		map = new int[R][C];
		air = new int[2]; // 공기청정기 두 줄

		int airIdx = 0;
		for (int i = 0; i < R; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < C; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
				if (map[i][j] == -1) {
					air[airIdx++] = i;
				}
			}
		}

		while (T-- > 0) {
			spreadDust();
			runAirCleaner();
		}

		System.out.println(countDust());
	}

	// 먼지 확산
	static void spreadDust() {
		int[][] temp = new int[R][C];

		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (map[i][j] > 0) {
					int spread = map[i][j] / 5;
					int cnt = 0;
					for (int d = 0; d < 4; d++) {
						int nr = i + dr[d];
						int nc = j + dc[d];

						if (nr < 0 || nr >= R || nc < 0 || nc >= C || map[nr][nc] == -1) continue;

						temp[nr][nc] += spread;
						cnt++;
					}
					temp[i][j] -= spread * cnt;
				}
			}
		}

		// 원래 map에 확산값 반영
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				map[i][j] += temp[i][j];
			}
		}
	}

	// 공기청정기 작동
	static void runAirCleaner() {
		int top = air[0];
		int bottom = air[1];

		// 위쪽 (반시계)
		for (int i = top - 1; i > 0; i--) map[i][0] = map[i - 1][0];
		for (int j = 0; j < C - 1; j++) map[0][j] = map[0][j + 1];
		for (int i = 0; i < top; i++) map[i][C - 1] = map[i + 1][C - 1];
		for (int j = C - 1; j > 1; j--) map[top][j] = map[top][j - 1];
		map[top][1] = 0;

		// 아래쪽 (시계)
		for (int i = bottom + 1; i < R - 1; i++) map[i][0] = map[i + 1][0];
		for (int j = 0; j < C - 1; j++) map[R - 1][j] = map[R - 1][j + 1];
		for (int i = R - 1; i > bottom; i--) map[i][C - 1] = map[i - 1][C - 1];
		for (int j = C - 1; j > 1; j--) map[bottom][j] = map[bottom][j - 1];
		map[bottom][1] = 0;
	}

	// 남은 먼지 양 계산
	static int countDust() {
		int sum = 0;
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (map[i][j] > 0) sum += map[i][j];
			}
		}
		return sum;
	}
}
