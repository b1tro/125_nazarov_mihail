import java.util.Scanner;

public interface BinaryOperation {
    Summa summa = new Summa();
    Multiplication mult = new Multiplication();
    Division div = new Division();
    Difference diff = new Difference();
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Введите операцию");
        String operation = input.nextLine();
        String whatIsOperation =  operation.replaceAll("[1234567890 ]","");
        String[] whatAreNumbers = (operation.replaceAll("[+-/*]"," ")).split(" ");
        int number1 = Integer.parseInt(whatAreNumbers[0]);
        int number2 = Integer.parseInt(whatAreNumbers[1]);
        switch(whatIsOperation)
        {
            case("+"):
                summa.summa(number1,number2);
                break;
            case("-"):
                diff.diff(number1,number2);
                break;
            case("*"):
                mult.mult(number1,number2);
                break;
            case("/"):
                div.div(number1,number2);
                break;
            default:
                System.out.println("Ошибка! Введен некорректеный знак");
                break;
        }
    }
}