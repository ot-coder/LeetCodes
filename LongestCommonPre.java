import java.util.Scanner;

class LongestCommonPre {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) {
            return "";
        }

        String prefix = strs[0];

        for (int i = 1; i < strs.length; i++) {
            while (strs[i].indexOf(prefix) != 0) {
                prefix = prefix.substring(0, prefix.length() - 1);
                
                if (prefix.isEmpty()) {
                    return "";
                }
            }
        }

        return prefix;
    }

    
    private String[] takeInput() {
        Scanner scanner = new Scanner(System.in);  
        System.out.println("Enter your words separated by space:");
        String input = scanner.nextLine();  
        return input.split(" ");  
    }

    public static void main(String[] args) {
       LongestCommonPre solution = new LongestCommonPre();
        
        String[] strs = solution.takeInput();
        
        
        System.out.println(solution.longestCommonPrefix(strs));
    }
}
