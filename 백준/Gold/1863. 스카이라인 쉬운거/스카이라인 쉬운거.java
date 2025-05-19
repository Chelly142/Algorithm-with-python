import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int n = Integer.parseInt(br.readLine());
		int[] skyline = new int[n];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			st.nextToken();
			int y = Integer.parseInt(st.nextToken());
			skyline[i] = y;
		}
		ArrayDeque<Integer> stack = new ArrayDeque<>();

		int answer = 0;
		for (int i = 0; i < n; i++) {
			int nowH = skyline[i];
			if(nowH==0){
				answer+=stack.size();
				stack.clear();
				continue;
			}
			if (stack.isEmpty()) {
				stack.add(nowH);
				continue;
			}
			
			while (true) {
				if(stack.isEmpty()) {
					stack.add(nowH);
					break;
				}
				int top = stack.peekLast();
				if (top < nowH) {
					stack.add(nowH);
					break;
				} else if (top > nowH) {
					stack.pollLast();
					answer++;
				} else {
					break;
				}
			}
		}
		answer += stack.size();
		System.out.println(answer);
	}

}
