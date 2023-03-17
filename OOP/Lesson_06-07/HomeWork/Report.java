public class Report {
    private User user;

    public Report(User user) {
        this.user = user;
    }

    public void printReport(User user) {
        System.out.println("Report for user: " + user.getName());
    }
}
