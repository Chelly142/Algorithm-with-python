import java.io.IOException;

public class Main {
    static int r, c;
    static byte[][] map;
    public static void main(String[] args) throws Exception {
        r = readInt();
        c = readInt();
        map = new byte[r][c];
        for (int i=0; i<r; i++) {
            System.in.read(map[i]);
            System.in.read();
        }
        int cnt = 0;
        for (int i=0; i<r; i++) {
            if (dfs(i, 0)) cnt++;
        }
        System.out.print(cnt);
    }
    static boolean dfs(int x, int y) {
        if (y == c-1) return true;
        map[x][y] = 'x';
        boolean valid = false;
        if (x > 0 && map[x-1][y+1] == '.') {
            valid = dfs(x-1, y+1);
        }
        if (valid) return true;
        if (map[x][y+1] == '.') {
            valid = dfs(x, y+1);
        }
        if (valid) return true;
        if (x < r-1 && map[x+1][y+1] == '.') {
            valid = dfs(x+1, y+1);
        }
        return valid;
    }
    static int readInt() throws IOException {
        int x = System.in.read() & 15;
        int y = System.in.read();
        while (y > 47) {
            x = (x << 3) + (x << 1) + (y & 15);
            y = System.in.read();
        }
        return x;
    }
}