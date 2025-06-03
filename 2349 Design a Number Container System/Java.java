class NumberContainers {

    Map<Integer, Integer> container_num = new HashMap<>();
    Map<Integer, TreeSet<Integer>> num_treeSetContainers = new HashMap<>();

    public NumberContainers() {

    }

    public void change(int index, int number) {
        if (container_num.containsKey(index)) {
            int prev_num = container_num.get(index);
            num_treeSetContainers.get(prev_num).remove(index);
            if (num_treeSetContainers.get(prev_num).isEmpty()) {
                num_treeSetContainers.remove(prev_num);
            }
        }
        container_num.put(index, number);
        num_treeSetContainers.putIfAbsent(number, new TreeSet<>());
        num_treeSetContainers.get(number).add(index);
    }

    public int find(int number) {
        return num_treeSetContainers.containsKey(number) ? num_treeSetContainers.get(number).first() : -1;
    }
}