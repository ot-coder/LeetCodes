import java.util.Scanner;

class palindrome {
    public boolean isPalindrome(int x) {
  
        if (x < 0) {
            return false;
        }

        int input = x;
        int reverse = 0;

        while (x != 0) {
            int lastDigit = x % 10;
            reverse = reverse * 10 + lastDigit;
            x /= 10;
        }

        return input == reverse;
        
    }

    private int takeInput() {
        Scanner scanner = new Scanner(System.in);
        System.out.println( "Enter your number: ");
        return scanner.nextInt();
    }


    public static void main(String[] args) {

        palindrome palindromeChecker = new palindrome();

        
        int userInput = palindromeChecker.takeInput();

       
        boolean result = palindromeChecker.isPalindrome(userInput);

        if (result) {
            System.out.println("True");
        }
        else {
            System.out.println("False");
        }

        
    }
}