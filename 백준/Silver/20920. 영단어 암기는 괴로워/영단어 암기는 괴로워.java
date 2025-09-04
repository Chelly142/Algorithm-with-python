import java.io.*;
import java.util.*;

public class Main {

    static class Word implements Comparable<Word> {
        String word;
        int freq;

        public Word(String word) {
            this.word = word;
            this.freq = 1;
        }

        @Override
        public int compareTo(Word o) {
            if (this.freq != o.freq) {
                return Integer.compare(o.freq, this.freq);
            }
            if (this.word.length() != o.word.length()) {
                return Integer.compare(o.word.length(), this.word.length());
            }
            return this.word.compareTo(o.word);
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (!(obj instanceof Word)) return false;
            Word other = (Word) obj;
            return this.word.equals(other.word);
        }

        @Override
        public int hashCode() {
            return Objects.hash(word);
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        Map<String, Word> map = new HashMap<>();

        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            if (s.length() < m) continue; 
            if (map.containsKey(s)) {
                map.get(s).freq++;
            } else {
                map.put(s, new Word(s));
            }
        }

        List<Word> list = new ArrayList<>(map.values());
        Collections.sort(list);

        StringBuilder sb = new StringBuilder();
        for (Word w : list) {
            sb.append(w.word).append('\n');
        }
        System.out.print(sb.toString());
    }
}
