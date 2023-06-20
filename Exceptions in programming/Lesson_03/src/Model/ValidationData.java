package Model;

public class ValidationData implements Validation {
    public boolean isValidGender(String gender) {
        if (gender.length() == 1) {
            if (gender.toLowerCase().contains("f") || gender.toLowerCase().contains("m")) {
                return true;
            }
            System.out.println("Принимаются только латинские буквы M и F");
            return false;
        }
        System.out.println("Длина должна быть не более 1 буквы!");
        return false;
    }

    public boolean isPhoneNumber(String data) {
        try {
            Integer.parseInt(data);
            return true;
        } catch (NumberFormatException e) {
            System.out.println("Номер телефона должен состоять только из цифр!");
            return false;
        }
    }


    public boolean isValidateDate(String date) {
        String regex = "\\d{2}\\.\\d{2}\\.\\d{4}";
        if (date.matches(regex)){
            return true;
        }
        System.out.println("Ввод не соответствует длине или формату dd.mm.yyyy");
        return false;
    }

    public boolean isValidName(String data) {
        return data.matches("[a-zA-Z]+");
    }
}
