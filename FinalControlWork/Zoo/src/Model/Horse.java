package Model;

public class Horse extends WildAnimal{
    private int speed;

    public Horse(String name, int age, boolean predator, int speed){
        super(name, age, predator);
        this.speed = speed;
    }

    public int getSpeed(){
    return speed;
    }

    public void setSpeed(int speed){
        this.speed = speed;
    }
}
