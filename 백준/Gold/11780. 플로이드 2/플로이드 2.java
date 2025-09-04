import java.io.*;
import java.util.*;

public class Main {

    static final int INF = (int)1e9;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        int[][] floyd = new int[n][n];
        ArrayList<Integer>[][] path = new ArrayList[n][n];
        

        
        for(int i= 0;i<n;i++) {
        	for(int j=0;j<n;j++) {
        		path[i][j] = new ArrayList<>();
        		if(i==j) {
        			floyd[i][j] = 0;
        		}else {
        			floyd[i][j] = INF;
        		}
        	}
        }

        for(int i = 0; i<m;i++) {
        	st = new StringTokenizer(br.readLine());
        	int a = Integer.parseInt(st.nextToken())-1;
        	int b = Integer.parseInt(st.nextToken())-1;
        	int c = Integer.parseInt(st.nextToken());
        	if(c<floyd[a][b]) {
        		floyd[a][b] = c;
        		path[a][b].clear();
        		path[a][b].add(a+1);
        	}
        	
        }
        
        
        for(int mid = 0; mid<n;mid++) {
        	for(int start = 0; start<n; start++) {
        		for(int end = 0; end<n;end++) {
        			if(floyd[start][end] >floyd[start][mid]+floyd[mid][end]) {
            			floyd[start][end] = floyd[start][mid]+floyd[mid][end];
            			path[start][end] = sumPath(path[start][mid],path[mid][end]);
        			}
        		}
        	}
        }
        
         for (int i = 0; i < n; i++) {
             for (int j = 0; j < n; j++) {
                 if (floyd[i][j] >= INF) System.out.print("0 ");
                 else System.out.print(floyd[i][j] + " ");
             }
             System.out.println();
         }
         for (int i = 0; i < n; i++) {
             for (int j = 0; j < n; j++) {
                 if (floyd[i][j] >= INF||i==j) System.out.print("0");
                 else {
                	 System.out.print(path[i][j].size()+1+" ");
                	 for(int k:path[i][j]) {
                		 System.out.print(k+" ");
                	 }
                	 System.out.print(j+1);
                 }
            	 System.out.println();
             }
         }
         

        
    }

	private static ArrayList<Integer> sumPath(ArrayList<Integer> path1, ArrayList<Integer> path2) {
		ArrayList<Integer> newPath = new ArrayList<>();
		newPath.addAll(path1);
		newPath.addAll(path2);
		return newPath;
	}
}
