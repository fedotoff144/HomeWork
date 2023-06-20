package Model;

public class DataMapper {
    public String map(Data data) {
        return String.format("%s %s %s %s %d %s ",
                data.getLastName(),
                data.getFirstName(),
                data.getSurname(),
                data.getBirthday(),
                data.getPhone(),
                data.getGender());
    }

}
