import java.sql.Date;

public class Perishable extends Product {
    private Date expireDate = new Date(2023 - 02 - 10);

    public Perishable(String name, double cost, Date expireDate) {
        super(name, cost);
        this.expireDate = expireDate;
    }

    @Override
    public String toString() {
        StringBuilder localstring = new StringBuilder(super.toString());
        localstring.append(String.format(" годен до %s", expireDate));
        return localstring.toString();
    }
}
