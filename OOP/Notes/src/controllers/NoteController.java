package controllers;

import model.Repository;
import model.Note;

import java.util.ArrayList;
import java.util.List;

public class NoteController {
    private final Repository repository;

    public NoteController(Repository repository) {
        this.repository = repository;
    }

    public void saveNote(Note note) throws Exception {
        repository.CreateNote(note);
    }

    public Note readNote(String noteId) throws Exception {
        List<Note> notes = repository.GetAllNotes();
        Note note = noteSearch(noteId, notes);
        return note;
    }

    private static Note noteSearch(String noteId, List<Note> notes) throws Exception {
        for (Note note : notes) {
            if (note.getId().equals(noteId)) {
                return note;
            }
        }
        throw new Exception("Note not found");
    }

    public void noteUpdate(String noteId, Note newNote) throws Exception {
        List<Note> notes = repository.GetAllNotes();
        Note note = noteSearch(noteId, notes);
        note.setHeader(newNote.getHeader());
        note.setText(newNote.getText());
        repository.SaveNote(notes);
    }

    public List<Note> readAllNotes() {
        return repository.GetAllNotes();
    }

    public void deleteNote(String readId) {
        List<Note> notes = repository.GetAllNotes();
        List<Note> newNote = new ArrayList<>();
        for (Note note : notes) {
            String tempId = note.getId();
            if (!tempId.equals(readId))
                newNote.add(note);
        }
        repository.SaveNote(newNote);
    }
}
