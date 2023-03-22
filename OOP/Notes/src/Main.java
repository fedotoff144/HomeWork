import controllers.NoteController;
import model.FileOperation;
import model.Repository;
import model.RepositoryFile;
import view.ViewNote;

public class Main {
    public static void main(String[] args) {

        FileOperation fileOperation = new FileOperation("notes.txt");
        Repository repository = new RepositoryFile(fileOperation);
        NoteController controller = new NoteController(repository);
        ViewNote view = new ViewNote(controller);
        view.run();
    }
}