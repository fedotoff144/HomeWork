package OOP.Lesson_02.zoo.Herbivores;

import OOP.Lesson_02.zoo.Runable;
import OOP.Lesson_02.zoo.Swimable;

public class Hipopotam extends Herbivores implements Swimable, Runable {
    private int swimSpeed = 10;
    private int speedRun = 5;

    public Hipopotam(String name) {
        super(name);
    }

    @Override
    public String say() {
        return "Buuaa";
    }

    @Override
    public int getSwimSpeed() {
        return this.swimSpeed;
    }
    @Override
    public int getSpeedRun() {
        return this.speedRun;
    }
}
