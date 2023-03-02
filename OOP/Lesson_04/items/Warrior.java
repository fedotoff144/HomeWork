package Lesson_04.items;

import Lesson_04.weapons.Weapon;
import Lesson_04.shield.Shield;

import java.util.Random;

public abstract class Warrior<T extends Weapon, E extends Shield> {
    private String name;
    protected T weapon;
    protected E shield;
    protected Random rnd = new Random();
    private int healthPoint;


    public Warrior(String name, T weapon, E shield) {
        this.name = name;
        this.weapon = weapon;
        this.shield = shield;
        healthPoint = 100 + shield.Protection();
    }

    public int getHealthPoint() {
        return healthPoint;
    }

    public void reduceHealthPoint(int damage) {
        this.healthPoint -= damage;
    }

    public int hitDamage(Warrior enemy) {
        int damage = rnd.nextInt(weapon.damage());
        enemy.reduceHealthPoint(damage);
        return damage;
    }

    public int getMaxDamage() {
        return weapon.damage();
    }

    public int getProtetion(){
        return shield.Protection();
    }

    @Override
    public String toString() {
        return "Warrior{" +
                "name='" + name + '\'' +
                ", weapon= " + weapon +
                ", shield - " + shield +
                ", healthPoint= " + healthPoint +
                '}';
    }
}
