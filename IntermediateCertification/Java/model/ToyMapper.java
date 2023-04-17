package model;

public class ToyMapper {
    public String map(Toy toy){ return String.format("%d;%s;%d",toy.getId(),toy.getName(),toy.getWinning());}

    public Toy map(String line){
        String[] lines = line.split(";");
        return new Toy(Integer.parseInt(lines[0]), lines[1], Integer.parseInt(lines[2]));
    }
}
