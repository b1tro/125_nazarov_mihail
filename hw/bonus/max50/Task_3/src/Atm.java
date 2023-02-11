public class Atm
{
    private int fifty_count;
    private int hundred_count;
    private int five_hundred_count;
    private int thousand_count;
    private int five_thousand_count;
    private int total_count;

    public void atm(int fifty_count, int hundred_count, int five_hundred_count, int thousand_count, int five_thousand_count)
    {
        this.fifty_count=fifty_count;
        this.hundred_count=hundred_count;
        this.five_hundred_count=five_hundred_count;
        this.thousand_count=thousand_count;
        this.five_thousand_count=five_thousand_count;
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

    public int getFive_thousand_count() {return five_thousand_count;}

    public void setFive_thousand_count(int five_thousand_count) {
        this.five_thousand_count = five_thousand_count;
    }

    public void load(int fifty_count, int hundred_count,  int five_hundred_count, int thousand_count,  int five_thousand_count)
    {
        this.total_count+=  fifty_count + hundred_count + five_hundred_count + thousand_count + five_thousand_count;
    }

    public boolean give(int summa)
    {
        if (summa%10 != 0)
        {
            return false;
        }
        if(summa>five_thousand_count)
        {
            five_thousand_count-=summa/5000;
            summa-=(summa/5000)*5000;
        }
        if(summa>thousand_count)
        {
            thousand_count-=summa/1000;
            summa-=(summa/1000)*1000;
        }
        if(summa>five_hundred_count)
        {
            five_hundred_count-=summa/500;
            summa-=(summa/500)*500;
        }
        if(summa>hundred_count)
        {
            hundred_count-=summa/100;
            summa-=(summa/100)*100;
        }
        if(summa>fifty_count)
        {
            fifty_count-=summa/50;
            summa-=(summa/50)*50;
        }
        if(summa !=0)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}


