package OOP.Lesson_02.zoo.Herbivores;

import OOP.Lesson_02.zoo.Flyable;

public class Cow extends Herbivores implements Flyable {
    private int flightSpeed = 13;
    private int flightHing = 2;

    public Cow(String name) {
        super(name);
    }

    @Override
    public String say() {
        return "Muu!";
    }

    @Override
    public int getSpeedFlyable() {
        return this.flightSpeed;
    }

    @Override
    public int getHigh() {
        return this.flightHing;
    }
}
