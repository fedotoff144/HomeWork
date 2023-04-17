import java.sql.Date;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class VendingMachine {
    protected List<Product> localList = new ArrayList<Product>();
    private double cash;

    public List<Product> getLocalList() {
        return localList;
    }

    public VendingMachine addProduct(Product inputProduct) {
        localList.add(inputProduct);
        inputProduct.setLoadDate(Date.valueOf(LocalDate.now()));
        return this;
    }

    @Override
    public String toString() {
        StringBuilder localString = new StringBuilder();
        for (Product item : localList) {
            localString.append(item.toString());
            localString.append("\n");
        }
        localString.append("money in machine: " + cash + "\n");
        return localString.toString();
    }

    public List<Product> findProduct(String name) {
        List<Product> foundProduct = new ArrayList<>();
        for (Product product : localList) {
            if (product.getName().contains(name)) {
                foundProduct.add(product);
            }
        }
        return foundProduct;
    }

    public Product sellProduct(Product sellingProduct) {
        Product sellProduct = new Product();
        if (localList.contains(sellingProduct)) {
            for (int i = 0; i < localList.size(); i++) {
                if (localList.get(i) == sellingProduct) {
                    sellProduct = localList.get(i);
                    cash += sellProduct.getCost();
                    localList.remove(i);
                    return sellProduct;
                }
            }
        }
        return sellProduct;
    }

}
