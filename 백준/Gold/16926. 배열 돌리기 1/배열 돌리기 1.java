import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	static int n, m, r;
	static int[][] arr;
	static int[][] copyArr;
	static final int[] dr = { 0, 1, 0, -1 };
	static final int[] dc = { -1, 0, 1, 0 };

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());

		arr = new int[n][m];
		copyArr = new int[n][m];

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		for (int t = 0; t < r; t++) {
			int nowR = 0;
			int nowC = 0;

			while (nowR < n / 2 && nowC < m / 2) {
				turn(nowR, nowC);
				nowR += 1;
				nowC += 1;
			}

			copyArray();
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				System.out.print(arr[i][j] + " ");
			}
			System.out.println();
		}
	}

	private static void turn(int startR, int startC) {
		int nowR = startR;
		int nowC = startC;
		int nowD = 0;

		int prevVal = arr[nowR][nowC]; // 시작값 저장

		while (true) {
			int nxtR = nowR + dr[nowD];
			int nxtC = nowC + dc[nowD];

			// 바깥 테두리를 벗어나는 경우 방향 전환
			if (nxtR < startR || nxtR >= n - startR || nxtC < startC || nxtC >= m - startC) {
				nowD = (nowD + 1) % 4;
				continue;
			}

			// 이동한 자리에 이전 값을 넣고, 현재 값을 다음으로 넘김
			copyArr[nxtR][nxtC] = prevVal;
			prevVal = arr[nxtR][nxtC];

			nowR = nxtR;
			nowC = nxtC;

			// 원래 자리로 돌아오면 종료
			if (nowR == startR && nowC == startC) break;
		}
	}


	private static void copyArray() {
		for (int i = 0; i < n; i++) {
			arr[i] = copyArr[i].clone();
		}
	}
}
