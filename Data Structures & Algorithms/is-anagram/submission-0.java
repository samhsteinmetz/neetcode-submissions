class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<String, Integer> skibidi = new HashMap<String, Integer>();
        HashMap<String, Integer> fortnite = new HashMap<String, Integer>();
        
        if(s.length() != t.length()){return false;}

        for(int i = 0; i < s.length(); i++){
            String sCurr = s.substring(i, i+1);
            if(skibidi.containsKey(sCurr)){
                skibidi.put(sCurr, skibidi.get(sCurr)+1);
            }else{
                skibidi.put(sCurr, 1);
            }

            String tCurr = t.substring(i, i+1);
            if(fortnite.containsKey(tCurr)){
                fortnite.put(tCurr, fortnite.get(tCurr)+1);
            }else{
                fortnite.put(tCurr, 1);
            }
        }

        for(String key : fortnite.keySet()){
            int val = fortnite.get(key);
            if(skibidi.containsKey(key) && skibidi.get(key) == val){

            }else{
                return false;
            }
        }

        return true;
    }
}
