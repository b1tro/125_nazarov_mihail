import java.util.HashMap;
import java.util.Scanner;

public class SummCalculator {

    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        System.out.println("Введите количество разных единиц товара");
        int totalCount = input.nextInt();
        System.out.println("Общая сумма покупки равна " + calculateSumm(totalCount));
 }
    public static int calculateSumm(int totalCount)
    {
        HashMap<String, Integer> namesAndCount = new HashMap<>();
        HashMap<String, Integer> namesAndPrice = new HashMap<>();
        namesAndCount.put("Капуста", 67);
        namesAndCount.put("Морковь", 69);
        namesAndCount.put("Огурцы", 27);
        namesAndCount.put("Бульба", 227);

        namesAndPrice.put("Капуста", 15);
        namesAndPrice.put("Морковь", 8);
        namesAndPrice.put("Огурцы", 13);
        namesAndPrice.put("Бульба", 3);

        int totalSum = 0;
        for (int i = 0; i != totalCount; i++)
        {
            Scanner input = new Scanner(System.in);
            System.out.println("Введи название товара");
            String thingName = input.nextLine();
            System.out.println("Введи количество");
            int thingCount = input.nextInt();
            while(thingCount > namesAndCount.get(thingName))
            {
                System.out.println("В данный момент в магазине всего " + namesAndCount.get(thingName) + " единиц " + thingName);
                System.out.println("Попробуйте взять меньше.");
                thingCount = input.nextInt();
            }
            System.out.println("Сумма данной покупки равна:" + (thingCount * namesAndPrice.get(thingName)));
            totalSum += thingCount * namesAndPrice.get(thingName);
        }
        return(totalSum);
    }
}
