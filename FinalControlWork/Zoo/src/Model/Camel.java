package Model;

public class Camel extends WildAnimal{
    private int distance;

    public Camel(String name, int age, boolean predator, int distance){
        super(name, age, predator);
        this.distance = distance;
    }

    public int getDistance(){
    return distance;
    }

    public void setDistance(int distance){
        this.distance = distance;
    }

}
