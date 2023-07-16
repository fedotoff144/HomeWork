package Model;

public class Donkey extends WildAnimal {
    private int liftingCapacity;

    public Donkey(String name, int age, boolean predator, int liftingCapacity){
        super(name, age, predator);
        this.liftingCapacity = liftingCapacity;
    }

    public int getLiftingCapacity(){
    return liftingCapacity;
    }

    public void setLiftingCapacity(int liftingCapacity){
        this.liftingCapacity = liftingCapacity;
    }

}
