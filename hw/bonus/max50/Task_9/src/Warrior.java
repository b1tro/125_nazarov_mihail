public abstract class Warrior {
    private String name;
    private int attack;
    public int health;

    public Warrior(String name, int attack,int health)
    {
        this.name = name;
        this.attack = attack;
        this.health = health;
    }

    public void setAttack(int attack) {
        this.attack = attack;
    }

    public int getAttack() {
        return attack;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setHealth(int health) {
        this.health = health;
    }

    public int getHealth() {
        return health;
    }
    public void takeDamage(int damage)
    {
        this.health -= damage;
    }

    public abstract void takeDamage(int damage, int armor);
}
