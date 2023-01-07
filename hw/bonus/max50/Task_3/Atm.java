public class Atm
{
    private int ten_count;
    private int fifty_count;
    private int hundred_count;
    private int two_hundred_count;
    private int five_hundred_count;
    private int thousand_count;
    private int two_thousand_count;
    private int five_thousand_count;
    private int total_count;

    public Atm()
    {
        this.ten_count = 0;
        this.fifty_count = 0;
        this.hundred_count = 0;
        this.two_hundred_count = 0;
        this.five_hundred_count = 0;
        this.thousand_count = 0;
        this.two_thousand_count = 0;
        this.five_thousand_count = 0;
    }

    public int getTen_count() {
        return ten_count;
    }

    public void setTen_count(int ten_count) {
        this.ten_count = ten_count;
    }

    public int getFifty_count() {
        return fifty_count;
    }

    public void setFifty_count(int fifty_count) {
        this.fifty_count = fifty_count;
    }

    public int getHundred_count() {
        return hundred_count;
    }

    public void setHundred_count(int hundred_count) {
        this.hundred_count = hundred_count;
    }

    public int getTwo_hundred_count() {
        return two_hundred_count;
    }

    public void setTwo_hundred_count(int two_hundred_count) {
        this.two_hundred_count = two_hundred_count;
    }

    public int getFive_hundred_count() {
        return five_hundred_count;
    }

    public void setFive_hundred_count(int five_hundred_count) {
        this.five_hundred_count = five_hundred_count;
    }

    public int getThousand_count() {
        return thousand_count;
    }

    public void setThousand_count(int thousand_count) {
        this.thousand_count = thousand_count;
    }

    public int getTwo_thousand_count() {
        return two_thousand_count;
    }

    public void setTwo_thousand_count(int two_thousand_count) {
        this.two_thousand_count = two_thousand_count;
    }

    public int getFive_thousand_count() {
        return five_thousand_count;
    }

    public void setFive_thousand_count(int five_thousand_count) {
        this.five_thousand_count = five_thousand_count;
    }

    public void load(int ten_count, int fifty_count, int hundred_count, int two_hundred_count, int five_hundred_count, int thousand_count, int two_thousand_count, int five_thousand_count)
    {
        this.total_count+= ten_count + fifty_count + hundred_count + two_hundred_count + five_hundred_count + thousand_count + two_thousand_count + five_thousand_count;
    }

    public void give(int count)
    {

    }
}
