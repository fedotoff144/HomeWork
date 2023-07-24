package Model.Animals;

import Model.WildAnimal;

public class Camel extends WildAnimal {
    private int distance;

    public Camel(int id, String name, int age, boolean predator, int distance) {
        super(id, name, age, predator);
        this.distance = distance;
    }

    public int getDistance() {
        return distance;
    }

    public void setDistance(int distance) {
        this.distance = distance;
    }

    @Override
    public String toString() {
        return "Camel {" +
                "id=" + getId() +
                ", name= " + getName() +
                ", age= " + getAge() +
                ", commands= " + getCommands() +
                ", predator= " + getPredator() +
                ", distance=" + distance +
                "}";
    }
}
