import controller.ToyMachineController;
import model.FileOperation;
import model.Repository;
import model.RepositoryFile;
import view.ToyMachineMenu;

public class Main {
    public static void main(String[] args) {
        FileOperation fileOperation = new FileOperation("Toyslist.csv");
        Repository repository = new RepositoryFile(fileOperation);
        ToyMachineController toyMachineController = new ToyMachineController(repository);
        ToyMachineMenu menu = new ToyMachineMenu(toyMachineController);
        menu.menu();
    }
}

