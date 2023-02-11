import java.util.*;

public class Dubler {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> mylist = new ArrayList<Integer>();
        while (scanner.hasNextInt()) {
            int k = scanner.nextInt();
            mylist.add(k);
        }
        int listSize = mylist.size() ;
        for (int i = 0; i < listSize; i++) {
            mylist.add(mylist.get(i));
        }
        Collections.sort(mylist);
    }
}

