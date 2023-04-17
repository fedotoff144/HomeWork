package view;

import java.util.Scanner;

public class ToyMachineMenu {


    public void menu(){
        Commands com;
        while (true){
            String command = prompt("Enter your command please: ");
            try{
                com = Commands.valueOf((command.toUpperCase()));
                if (com == Commands.EXIT)
                    return;
                switch (com){
                    case ADD_TOYS -> System.out.println("ADD_TOYS");
                    case WIN_TOY -> System.out.println("WIN_TOY");
                    case VIEW -> System.out.println("VIEW");
                    case HELP -> System.out.println("HELP");
                }
            }
            catch (Exception e){
                System.out.println(e.getMessage());
            }
        }

    }

    public String prompt(String massage){
        Scanner scn = new Scanner(System.in);
        System.out.println(massage);
        return scn.nextLine();
    }
}
