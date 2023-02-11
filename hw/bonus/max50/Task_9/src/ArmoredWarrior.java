public class ArmoredWarrior extends Warrior {
private int armor;
    public ArmoredWarrior(String name, int attack, int health) {
        super(name, attack, health);
    }

    public void setArmor(int armor) {
        this.armor = armor;
    }

    public int getArmor() {
        return armor;
    }

    @Override
    public void takeDamage(int damage, int armor) {
        if (damage - armor >= 1)
        {
            super.takeDamage(damage - armor);
        }
    }
}
