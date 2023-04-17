import java.sql.Date;

public class Product {
    private String name;
    private double cost;
    private Date loadDate;

    public Product(String name, double cost) {
        this.name = name;
        this.cost = cost;
    }

    public Product() {
        this("0", 0D);
    }

    public void setLoadDate(java.util.Date date) {
        this.loadDate = loadDate;
    }

    @Override
    public String toString() {
        return String.format("Наименование: %s, стоимость: %f, дата загрузки: %s", name, cost, loadDate);
    }

    public String getName() {
        return name;
    }

    public double getCost() {
        return cost;
    }

    @Override
    public boolean equals(Object obj) {
        return (this.name.equals(((Product) obj).name) && (this.cost == (((Product) obj).cost)));

    }

    @Override
    public int hashCode() {
        return name.hashCode() + (int) cost;
    }
}
