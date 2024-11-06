class stairs70 {
    public int climbStairs(int n) {
        return climbStairs(n, new int[n + 1]);
    }

    private int climbStairs(int n, int[] newa) {
            if (n == 0 || n == 1) 
            return 1;
            if (newa[n] !=0)
            return newa[n];

        return newa[n] =climbStairs(n - 1, newa) + climbStairs(n - 2, newa);
    };
}