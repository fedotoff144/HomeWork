package view;

import controllers.NoteController;
import model.Note;

import java.util.List;
import java.util.Scanner;

public class ViewNote {
    private final NoteController noteController;

    public ViewNote(NoteController noteController) {
        this.noteController = noteController;
    }

    public void run() {
        Commands com;
        while (true) {
            String command = prompt("Enter command: ");
            try {
                com = Commands.valueOf(command.toUpperCase());
                if (com == Commands.EXIT)
                    return;
                switch (com) {
                    case CREATE:
                        create();
                        break;
                    case READ:
                        read();
                        break;
                    case LIST:
                        list();
                        break;
                    case UPDATE:
                        noteUpdate();
                        break;
                    case DELETE:
                        deleteNote();
                        break;
                }
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        }
    }

    private void deleteNote() {
        String readId = getID("Enter ID note: ");
        noteController.deleteNote(readId);
    }

    private String getID(String message) {
        String readId = prompt(message);
        return readId;
    }

    private void noteUpdate() throws Exception {
        String readID = prompt("Input ID note for edit: ");
        noteController.noteUpdate(readID, inputNote());
    }

    private void list() {
        List<Note> listNotes = noteController.readAllNotes();
        for (Note note : listNotes) {
            System.out.println(note + "\n");
        }
    }

    private void read() throws Exception {
        String id = prompt("Identification note: ");
        Note note = noteController.readNote(id);
        System.out.println(note);
    }

    private Note inputNote() {
        String header = prompt("Header: ");
        String text = prompt("Text: ");
        return new Note(header, text);
    }

    private void create() throws Exception {
        noteController.saveNote(inputNote());
    }

    private String prompt(String message) {
        Scanner in = new Scanner(System.in);
        System.out.print(message);
        return in.nextLine();
    }
}
