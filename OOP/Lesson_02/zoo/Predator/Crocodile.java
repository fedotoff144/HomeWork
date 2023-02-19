package OOP.Lesson_02.zoo.Predator;

import OOP.Lesson_02.zoo.Flyable;
import OOP.Lesson_02.zoo.Runable;

public class Crocodile extends Predator implements Runable, Flyable {
    private int flightSpeed = 15;
    private int flightHing = 5;
    private int runSpeed = 100;

    public Crocodile(String name) {
        super(name);
    }

    @Override
    public String say() {
        return "Shhhhh";
    }

    @Override
    public int getSpeedFlyable() {
        return this.flightSpeed;
    }

    @Override
    public int getHigh() {
        return this.flightHing;
    }

    @Override
    public int getSpeedRun() {
        return this.runSpeed;
    }
}
