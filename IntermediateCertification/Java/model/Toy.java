package model;

public class Toy {

    private int id;
    private String name;
    private int winning;

    public Toy(int id, String name, int winning){
        this.id = id;
        this.name = name;
        this.winning = winning;
    }

    public int getId() {
        return id;
    }

    public String getName(){
        return name;
    }

    public void setName(String name){
        this.name = name;
    }

    public void setWinning(int winning) {
        this.winning = winning;
    }

    public int getWinning(){
        return winning;
    }





    @Override
    public String toString() {
        return "model.Toy{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", winning=" + winning +
                '}';
    }
}

