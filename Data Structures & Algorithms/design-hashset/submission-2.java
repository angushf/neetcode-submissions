class MyHashSet {
    int size;
    Integer[][] buckets;

    public MyHashSet() {
        this.size = 1000;
        this.buckets = new Integer[1000][1];
    }

    private int hash(int key) {
        return key % this.size; // returns index between 0 - (size of buckets - 1)
    }
    
    public void add(int key) {
        if (this.contains(key)) {
            return; // HashSet already contains key - nothing to do
        }

        int index = this.hash(key);

        this.buckets[index][0] = key;
    }
    
    public void remove(int key) {
        if (!this.contains(key)) {
            return; // key not in hashset - do nothing
        }

        int index = this.hash((Integer) key);
        this.buckets[index][0] = null;
    }
    
    public boolean contains(int key) {
        int index = this.hash(key);
        Integer elementAtIndex = this.buckets[index][0];

        if (elementAtIndex != null && elementAtIndex.equals((Integer) key)) {
            return true;
        } else {
            return false;
        }
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */