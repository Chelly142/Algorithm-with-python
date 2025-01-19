class Solution {
    public int solution(int number, int limit, int power) {
        int answer = 0;
        for(int i=1;i<=number;i++){
            int price = calcPrice(i,limit,power);
            answer+=price;
        }
        return answer;
    }
    
    
    
    
    public int calcPrice(int n, int limit, int power){
        int subCount =calcDivisorCount(n);
        if(subCount>limit){
            return power;
        }
        return subCount;
    }
    
    public int calcDivisorCount(int n){
        double sqrt = Math.sqrt(n);
        int count = 0;
        for(int i = 1; i<=sqrt;i++){
            if(n%i==0){
                count++;
                if(i!=n/i){
                    count++;
                }
            }
            
        }
        return count;
    }
}