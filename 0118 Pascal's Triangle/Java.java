class Solution {
    public List<List<Integer>> generate(int numRows) {
      List<List<Integer>> res = new ArrayList<>();
        res.add(List.of(1));
        if (numRows > 1) res.add(List.of(1, 1));
        for (int i = 3 ; i <= numRows ; i++) {
            List<Integer> nextRow = new ArrayList<>();
            List<Integer> prevRow = res.get(res.size() - 1);
            nextRow.add(1);
            for (int j = 0 ; j < prevRow.size() - 1 ; j++) {
                nextRow.add(prevRow.get(j) + prevRow.get(j + 1));
            }
            nextRow.add(1);
            res.add(nextRow);
        }
        return res;
    }
}