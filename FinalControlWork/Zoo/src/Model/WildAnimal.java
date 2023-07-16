package Model;

public class WildAnimal extends Animal{
    private boolean predator;


    public WildAnimal(String name, int age, boolean predator) {
        super(name, age);
        this.predator = predator;
    }

    public boolean getPredator(){
        return predator;
    }

    public void setPredator(boolean predator){
        this.predator = predator;
    }

}
