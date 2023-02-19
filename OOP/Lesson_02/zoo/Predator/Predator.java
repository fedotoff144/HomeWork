package OOP.Lesson_02.zoo.Predator;

import OOP.Lesson_02.zoo.Animal;

public abstract class Predator extends Animal{
    public Predator(String name) {
        super(name);
    }

    @Override
    public String feed() {
        return "meat";
    }


}