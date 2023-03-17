
/*
 * Single Responsibility Principle
 * Open-Closed Principle
 * Liskov Substitution Principle
 * Interface Segregation Principle
 * Dependency Inversion Principle
 */

public class Main {
    public static void main(String[] args) {
        User user = new User("Bob");
        Report report = new Report(user);

        report.printReport(user);
        user.save(new Persister(user));
    }
}