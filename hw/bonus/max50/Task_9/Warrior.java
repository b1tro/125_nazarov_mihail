public class Warrior {
    private String name;
    private int attack;
    private int health;

    public void Warrior(String name, int attack, int health)
    {
        this.name = name;
        this.attack = attack;
        this.health = health;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAttack() {
        return attack;
    }

    public int getHealth() {
        return health;
    }

    public void setAttack(int attack) {
        this.attack = attack;
    }

    public void setHealth(int health) {
        this.health = health;
    }
    public takeDamage(Warrior warrior1, Warrior warrior2)
    {
        warrior1.health-=warrior2.attack;
    }

}
