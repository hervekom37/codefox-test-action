
/* DEMO FILE: Dangerous SQL concatenation */
import java.sql.*;

public class UnsafeQuery {
    public static void main(String[] args) {
        try {
            String userInput = "alice'; DROP TABLE users; --";
            String sql = "SELECT * FROM users WHERE name = '" + userInput + "'";
            System.out.println("Executing: " + sql);
            // Not actually connecting here, this is for demo purposes
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}