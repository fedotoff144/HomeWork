package Model.Animals;

import Model.WildAnimal;

public class Donkey extends WildAnimal {
    private int liftingCapacity;

    public Donkey(int id, String name, int age, boolean predator, int liftingCapacity) {
        super(id, name, age, predator);
        this.liftingCapacity = liftingCapacity;
    }

    public int getLiftingCapacity() {
        return liftingCapacity;
    }

    public void setLiftingCapacity(int liftingCapacity) {
        this.liftingCapacity = liftingCapacity;
    }

    @Override
    public String toString() {
        return "Donkey {" +
                "id=" + getId() +
                ", name= " + getName() +
                ", age= " + getAge() +
                ", commands= " + getCommands() +
                ", predator= " + getPredator() +
                ", liftingCapacity=" + liftingCapacity +
                "}";
    }
}
