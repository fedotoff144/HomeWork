package Model;

public class WildAnimal extends Animal {
    private boolean predator;


    public WildAnimal(int id, String name, int age, boolean predator) {
        super(id, name, age);
        this.predator = predator;
    }

    public boolean getPredator() {
        return predator;
    }

    public void setPredator(boolean predator) {
        this.predator = predator;
    }

//    @Override
//    public String toString() {
//        return "WildAnimal{" +
//                "predator=" + predator +
//                '}';
//    }
}
