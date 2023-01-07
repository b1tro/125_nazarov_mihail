public class Student
{
    private String name;
    private int age;
    private String group;
    private double mean_score;

    public Student(String name, int age, String group, double mean_score)
    {
        this.name = name;
        this.age = age;
        this.group = group;
        this.mean_score = mean_score;
    }
    Student me = new Student("Michail Nazarov", 18, "125", 0);

    public void getName()
    {
        return name;
    }
    public void setName(String name)
    {
        this.name = name;
    }

    public void getAge()
    {
        return age;
    }
    public void setAge(int age)
    {
        this.age = age;
    }

    public void getGroup()
    {
        return group;
    }
    public void setGroup(String group)
    {
        this.group = group;
    }

    public void getMean_score()
    {
        return mean_score;
    }
    public void setMean_score(double mean_score)
    {
        this.mean_score = mean_score;
    }
}
