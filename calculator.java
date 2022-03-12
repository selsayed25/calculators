// This calculator was coded by Sami Elsayed
import java.util.Scanner;

public class calculator {
    public static void main(String[] args) {
        char operator;
        Double number_one, number_two, result;
        Scanner input = new Scanner(System.in);

        System.out.println("Choose an operator: ");
        System.out.println("Addition (+): ");
        System.out.println("Subtraction (-): ");
        System.out.println("Multiplication (*): ")
        System.out.println("Division (/): ")
        operator = input.next().charAt(0);

        System.out.println("Enter first number: ")
        number_one = input.nextDouble();

        System.out.println("Enter second number: ")
        number_two = input.nextDouble();

        switch (operator) {
            case '+':
                result = number_one + number_two;
                System.out.println(number_one + " + " + number_two + " = " + result);
                break;

            case '-':
                result = number_one - number_two;
                System.out.println(number_one + " - " + number_two + " = " + result);
                break;

            case '*':
                result = number_one * number_two;
                System.out.println(number_one + " * " + number_two + " = " + result);
                break;
            
            case '/':
                result = number_one / number_two;
                System.out.println(number_one + " / " + number_two + " = " + result);
                break;

            default:
                System.out.println("Invalid operator!");
                break;
        }

        input.close();
    }
}
