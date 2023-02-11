import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;

public class TimeController {
    public static void main(String[] args)
    {
        ArrayList<String> clubs = new ArrayList<String>();
        ArrayList<Integer> time = new ArrayList<Integer>();
        clubs.add("Волейбол");
        clubs.add("Хоккей");
        clubs.add("Баскетбол");
        clubs.add("Футбол");
        clubs.add("Гандбол");

        time.add(90);
        time.add(270);
        time.add(1000);
        time.add(457);
        time.add(30);

        System.out.println("Название занятия с максимальным  суммарным временем: " + (getActionWithMaxTime(clubs,time)));
    }
    public static String getActionWithMaxTime(ArrayList<String> clubs, ArrayList<Integer> time)
    {
        return clubs.get(time.indexOf(Collections.max(time)));
    }
}
