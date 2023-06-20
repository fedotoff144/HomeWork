package Model;

public class Data {
    private String lastName;
    private String firstName;
    private String surname;
    private String birthday;
    private Integer phone;
    private String gender;

    public Data(String lastName, String firstName, String surname, String birthday, Integer phone, String gender){
        this.lastName = lastName;
        this.firstName = firstName;
        this.surname = surname;
        this.birthday = birthday;
        this.phone =phone;
        this.gender = gender;
    }

    public String getLastName() {
        return lastName;
    }

    public String getFirstName() {
        return firstName;
    }

    public String getSurname() {
        return surname;
    }

    public String getBirthday() {
        return birthday;
    }

    public Integer getPhone() {
        return phone;
    }

    public String getGender() {
        return gender;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }

    public void setBirthday(String birthday) {
        this.birthday = birthday;
    }

    public void setPhone(Integer phone) {
        this.phone = phone;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    @Override
    public String toString() {
        return "Data{" +
                "lastName='" + lastName + '\'' +
                ", firstName='" + firstName + '\'' +
                ", surname='" + surname + '\'' +
                ", birthday='" + birthday + '\'' +
                ", phone=" + phone +
                ", gender='" + gender + '\'' +
                '}';
    }
}
