import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
public class Counter {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Количество чисел массива?");
        int size = input.nextInt();
        int array[] = new int[size];
        System.out.println("Вводи числа!");
        for (int i = 0; i < size; i++) {
            array[i] = input.nextInt();
        }
        System.out.print ("Массив заполнен.");
        Map<Integer, Integer> counter = new HashMap<>();
        for (int x : array) {
            int newValue = counter.getOrDefault(x, 0) + 1;
            counter.put(x, newValue);
        }
        System.out.println(counter);
    }
    }

