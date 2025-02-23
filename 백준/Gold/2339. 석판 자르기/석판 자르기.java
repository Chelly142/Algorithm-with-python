import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
    static int n;
    static int[][] map;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        map = new int[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int ver = dnc(0, 0, 0, n, n);
        int hor = dnc(1, 0, 0, n, n);

        int result = ver + hor;
        System.out.println(result > 0 ? result : -1);
    }

    private static int dnc(int mod, int r, int c, int sizeR, int sizeC) {
        int dust = 0;
        int dia = 0;

        for (int i = r; i < r + sizeR; i++) {
            for (int j = c; j < c + sizeC; j++) {
                if (map[i][j] == 1) {
                    dust++;
                } else if (map[i][j] == 2) {
                    dia++;
                }
            }
        }

        if (dia == 0 || (dust == 0 && dia >= 2) || (dia == 1 && dust >= 1)) {
            return 0;
        }
        if (dia == 1 && dust == 0) {
            return 1;
        }

        int result = 0;
        for (int i = 0; i < sizeR; i++) {
            for (int j = 0; j < sizeC; j++) {
                if (map[r + i][c + j] == 1 && isDia(r + i, c + j, mod, r, c, sizeR, sizeC)) {
                    int numZero, numOne;

                    if (mod == 0) {
                        if (j == sizeC-1 || j == 0) //만약 불순물이 외곽에 있을경우 자르지 못한다. *석판은 무조건 두조각으로 나뉘어야한
                            continue;
                        numZero = dnc(1, r, c, sizeR, j);
                        numOne = dnc(1, r, c + j + 1, sizeR, sizeC - j - 1);
                    } else {
                        if (i == sizeR-1 || i == 0) //만약 불순물이 외곽에 있을경우 자르지 못한다. *석판은 무조건 두조각으로 나뉘어야한
                            continue;
                        numZero = dnc(0, r, c, i, sizeC);
                        numOne = dnc(0, r + i + 1, c, sizeR - i - 1, sizeC);
                    }
                    result += numZero * numOne;
                }
            }
        }
        return result;
    }

    private static boolean isDia(int x, int y, int mod, int r, int c, int sizeR, int sizeC) {
        if (mod == 0) {
            for (int i = r; i < r + sizeR; i++) {
                if (map[i][y] == 2) {
                    return false;
                }
            }
        } else {
            for (int j = c; j < c + sizeC; j++) {
                if (map[x][j] == 2) {
                    return false;
                }
            }
        }
        return true;
    }
}
