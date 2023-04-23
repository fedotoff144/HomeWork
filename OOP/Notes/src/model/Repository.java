package model;


import java.util.List;

public interface Repository {
    String CreateNote(Note note, List<Note> notes);

    List<Note> GetAllNotes();

    void SaveNote(List<Note> notes);
}
