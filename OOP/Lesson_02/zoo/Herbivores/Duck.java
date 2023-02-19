package OOP.Lesson_02.zoo.Herbivores;

import OOP.Lesson_02.zoo.Flyable;
import OOP.Lesson_02.zoo.Runable;

public class Duck extends Herbivores implements Flyable, Runable {
    private int flightSpeed = 15;
    private int flightHing = 5;
    private int runSpeed = 10;

    public Duck(String name) {
        super(name);
    }

    @Override
    public String say() {
        return "Krya Krya!";
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