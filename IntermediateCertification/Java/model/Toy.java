package model;

public class Toy {

    private int id;
    private String name;
    private int winning;

    public Toy(int id, String name, int winning) {
        this.id = id;
        this.name = name;
        this.winning = winning;
    }

    public Toy() {

    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setWinning(int winning) {
        this.winning = winning;
    }

    public int getWinning() {
        return winning;
    }


    @Override
    public String toString() {
        return "Игрушка " +
                "№ " + id +
                ", название-'" + name + '\'' +
                ", вероятность выигрыша " + winning +
                '%';
    }
}

