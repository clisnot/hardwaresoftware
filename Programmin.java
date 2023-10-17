import javax.swing.JOptionPane;

public class main {

 public static void main(string[] args) {
//  JOptionPane. showMessageDialog(null, "Hello World");
  String word = JOptionPane.showInputDialog(null, "Please type your age:");
  double age = Double.parseDouble(word);
  JOptionPane.showMessageDialog(null, "You are ") + age + " years old.");
  System.exit(0);
 }

}
