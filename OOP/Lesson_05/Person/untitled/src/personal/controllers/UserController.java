package personal.controllers;

import personal.model.Repository;
import personal.model.User;
import personal.views.Validation;

import java.util.ArrayList;
import java.util.List;

public class UserController {
    private final Repository repository;
    private final Validation validator;

    public UserController(Repository repository, Validation validator) {
        this.validator = validator;
        this.repository = repository;
    }

    public void saveUser(User user) throws Exception {
        validator.validateUser(user);
        repository.CreateUser(user);
    }

    public User readUser(String userId) throws Exception {
        List<User> users = repository.getAllUsers();
        User user = userSearch(userId, users);
        return user;
    }

    private static User userSearch(String userId, List<User> users) throws Exception {
        for (User user : users) {
            if (user.getId().equals(userId)) {
                return user;
            }
        }
        throw new Exception("User not found");
    }

    public List<User> readAllUsers() {
        return repository.getAllUsers();
    }

    public void updateUser(String userId, User newUser) throws Exception {
        validator.validateUser(newUser);
        List<User> users = repository.getAllUsers();
        User user = userSearch(userId, users);
        user.setFirstName(newUser.getFirstName());
        user.setLastName(newUser.getLastName());
        user.setPhone(newUser.getPhone());
        repository.saveUsers(users);
    }

    public void deleteUser(String readId) {
        List<User> users = repository.getAllUsers();
        List<User> newUsers = new ArrayList<>();
        for (User user : users) {
            String tempId = user.getId();
            if (!tempId.equals(readId))
                newUsers.add(user);
        }
        repository.saveUsers(newUsers);
    }
}
