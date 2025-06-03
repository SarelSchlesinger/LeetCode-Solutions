class Solution {
    
    public int manhattanDistance(int x1, int y1, int x2, int y2) {
        return Math.abs(x1 - x2) + Math.abs(y1 - y2);
    }

    public int[][] allCellsDistOrder(int rows, int cols, int rCenter, int cCenter) {
        return IntStream.range(0, rows)
                        .boxed()
                        .flatMap(i -> IntStream.range(0, cols)
                                               .mapToObj(j -> new int[]{ i, j }))
                        .sorted(Comparator.comparingInt(position -> manhattanDistance(position[0], position[1], rCenter, cCenter)))
                        .toArray(int[][]::new);
    }
}