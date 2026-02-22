class Spreadsheet {

    private int[][] mat;

    public Spreadsheet(int rows) {
        this.mat = new int[26][rows];
    }
    
    public void setCell(String cell, int value) {
        mat[cell.charAt(0) - 'A'][Integer.parseInt(cell.substring(1)) - 1] = value;
    }
    
    public void resetCell(String cell) {
        setCell(cell, 0);
    }
    
    public int getValue(String formula) {
        String[] s = formula.substring(1).split("\\+", 2);
        return Arrays.stream(s).mapToInt(i -> Character.isLetter(i.charAt(0)) ? mat[i.charAt(0) - 'A'][Integer.parseInt(i.substring(1)) - 1] : Integer.parseInt(i)).sum();
    }
}