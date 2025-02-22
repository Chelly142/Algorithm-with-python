
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


class Main {
    static int n;
    static int[] magicalNum;
    static final int[] firstNums = {2, 3, 5, 7};
    static final int[] nonFirstNums = {1, 3, 7, 9};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        n = Integer.parseInt(br.readLine());
        magicalNum = new int[n];

        back(0);
    }

    private static void back(int cnt) {
        if (cnt == n) {
            for (int j : magicalNum) {
                System.out.print(j);
            }
            System.out.println();
            return;
        }

        if (cnt == 0) { // 2,3,5,7 중 하나여서 반드시 소수
            for (int i : firstNums) {
                magicalNum[cnt] = i;
                back(cnt + 1);
            }
        } else {
            for (int i : nonFirstNums) {
                magicalNum[cnt] = i;
                if (isMagical(cnt)) { //추가된 수 포함해서 소수인지 판별
                    back(cnt + 1);
                }
            }
        }

    }

    private static boolean isMagical(int cnt) {
        int num = 0;
        for (int i = 0; i <= cnt; i++) {
            num += (int) (magicalNum[i] * Math.pow(10, cnt - i));
        }

        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {

                return false;
            }
        }
        return true;
    }
}