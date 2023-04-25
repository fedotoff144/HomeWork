package view;

import controller.ToyMachineController;

import java.util.Scanner;

public class ToyMachineMenu {
    ToyMachineController toyMachineController;

    public ToyMachineMenu(ToyMachineController toyMachineController) {
        this.toyMachineController = toyMachineController;
    }

    public void menu() {
        Commands com;
        while (true) {
            System.out.println("\n<<<<<< Автомат игрушек >>>>>>\nКоманды для выбора: ADD_TOYS, WIN_TOY, VIEW_TOYS, HELP, EXIT");
            System.out.println("-------------------------------------------------------------");
            String command = prompt("Введите вашу команду: ");
            try {
                com = Commands.valueOf(command.toUpperCase());
                switch (com) {
                    case ADD_TOYS: {
                        addToys();
                        break;
                    }
                    case WIN_TOY: {
                        toyMachineController.winToy();
                        break;
                    }
                    case VIEW_TOYS: {
                        toyMachineController.viewAllToys();
                        break;
                    }
                    case HELP: {
                        toyMachineController.help();
                        break;
                    }
                    case EXIT:
                        return;
                }
            } catch (Exception ex) {
                viewErrorMessage(ex.getMessage());
            }
        }

    }

    private void addToys() {
        String nameToy = prompt("Введите название игрушки: ");
        int count = Integer.parseInt(prompt("Введите количество: "));
        toyMachineController.addToy(nameToy, count);
    }

    private void viewErrorMessage(String textError) {
        boolean flagMessage = textError.contains("No enum constant");
        if (flagMessage) {
            System.out.println("Комманда не найдена");
        } else {
            System.out.println(textError);
        }
    }


    public static String prompt(String massage) {
        Scanner scn = new Scanner(System.in);
        System.out.print(massage);
        return scn.nextLine();
    }
}
