package Lesson_04.items;

import Lesson_04.shield.Raincoat;
import Lesson_04.weapons.Bow;

public class Archer extends Warrior<Bow, Raincoat> implements DistanceAttacker {
    private int distance;

    public Archer(String name, Bow weapon, Raincoat shield) {
        super(name, weapon, shield);

        distance = weapon.getDistance() + rnd.nextInt(10);
    }

    public int getDistance() {
        return distance;
    }

    @Override
    public String toString() {
        return super.toString() + " Type = Archer{" +
                "distance = " + distance +
                '}';
    }
}