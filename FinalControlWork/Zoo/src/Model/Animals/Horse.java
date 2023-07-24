package Model.Animals;

import Model.WildAnimal;

public class Horse extends WildAnimal {
    private int speed;

    public Horse(int id, String name, int age, boolean predator, int speed){
        super(id, name, age, predator);
        this.speed = speed;
    }

    public int getSpeed(){
    return speed;
    }

    public void setSpeed(int speed){
        this.speed = speed;
    }

    @Override
    public String toString() {
        return "Horse {" +
                "id=" + getId() +
                ", name= " + getName() +
                ", age= " + getAge() +
                ", commands= " + getCommands() +
                ", predator= " + getPredator() +
                ", speed= " + speed +
                "}";
    }
}
