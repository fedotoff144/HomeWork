package OOP.Lesson_02.zoo.Herbivores;

import OOP.Lesson_02.zoo.Runable;

public class Goat extends Herbivores implements Runable{
    private int runSpeed = 4;
    public Goat(String name) {
        super(name);
    }

    @Override
    public String say() {
        return "Beee!";
    }

    @Override
    public int getSpeedRun() {
        return this.runSpeed;
    }
}