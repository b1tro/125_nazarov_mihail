public class ArmoredWarrior extends Warrior{
    private int armor;

    public int getArmor() {
        return armor;
    }

    public void setArmor(int armor) {
        this.armor = armor;
    }

    super(name, attack, health);
    this.armor=armor;
    @Override
    public takeDamage(ArmoredWarrior armored_warrior1, Warrior warrior2, )
    {
        if (warrior2.attack - armor <= 0)
        {
            warrior2.attack = 1;
        }
        else {
            warrior2.attack-=armor;
        }
    }
}
