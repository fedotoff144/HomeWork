package view;

import controller.ToyMachineController;
import model.Toy;

import java.util.Scanner;

public class ToyMachineMenu {
    ToyMachineController toyMachineController;

    public ToyMachineMenu(ToyMachineController toyMachineController){
        this.toyMachineController = toyMachineController;
    }

    public void menu(){
        Commands com;
        while (true){
            System.out.println("\n<<<<<< Автомат игрушек >>>>>>\nКоманды для выбора: ADD_TOYS, WIN_TOY, VIEW_TOYS, HELP, EXIT");
            System.out.println("-------------------------------------------------------------");
            String command = prompt("Введите вашу команду пожалуйста: ");
            try{
                com = Commands.valueOf((command.toUpperCase()));
                if (com == Commands.EXIT)
                    return;
                switch (com){
                    case ADD_TOYS -> System.out.println("ADD_TOYS");
                    case WIN_TOY -> System.out.println("WIN_TOY");
                    case VIEW_TOYS -> System.out.println("VIEW_TOYS");
                    case HELP -> toyMachineController.help();
                }
            }
            catch (Exception e){
                System.out.println(e.getMessage());
            }
        }

    }

    private Toy inputToy(){
        String nameToy = prompt("Введите наименование игрушки: ");
        return new Toy(nameToy);
    }

    public String prompt(String massage){
        Scanner scn = new Scanner(System.in);
        System.out.println(massage);
        return scn.nextLine();
    }
}
