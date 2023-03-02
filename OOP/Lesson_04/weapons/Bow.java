package Lesson_04.weapons;

public class Bow implements Weapon {

    private int distance = 30;

    public int getDistance() {
        return distance;
    }

    @Override
    public int damage() {
        return 50;
    }

    @Override
    public String toString() {
        return "Bow{" +
                "damage= " + damage() +
                ", distance= " + distance +
                '}';
    }
}