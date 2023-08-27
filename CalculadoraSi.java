import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class CalculadoraSi {
    private JFrame frame;
    private JTextField textField;
    private double num1 = 0;
    private String operator = "";
    private boolean isOperatorClicked = false;

    public CalculadoraSi() {
        frame = new JFrame("Simple Calculator");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 400);
        frame.setLayout(new BorderLayout());

        textField = new JTextField();
        textField.setEditable(false);
        frame.add(textField, BorderLayout.NORTH);

        JPanel buttonPanel = new JPanel();
        buttonPanel.setLayout(new GridLayout(4, 4, 10, 10));

        String[] buttonLabels = {
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        };

        for (String label : buttonLabels) {
            JButton button = new JButton(label);
            button.addActionListener(new ButtonClickListener());
            buttonPanel.add(button);
        }

        frame.add(buttonPanel, BorderLayout.CENTER);
        frame.setVisible(true);
    }

    private class ButtonClickListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            String command = e.getActionCommand();

            if (command.matches("[0-9]")) {
                if (isOperatorClicked) {
                    textField.setText("");
                    isOperatorClicked = false;
                }
                textField.setText(textField.getText() + command);
            } else if (command.matches("[+\\-*/]")) {
                if (!operator.isEmpty()) {
                    calculateResult();
                }
                num1 = Double.parseDouble(textField.getText());
                operator = command;
                isOperatorClicked = true;
            } else if (command.equals("=")) {
                calculateResult();
                operator = "";
            } else if (command.equals(".")) {
                if (!textField.getText().contains(".")) {
                    textField.setText(textField.getText() + ".");
                }
            }
        }

        private void calculateResult() {
            double num2 = Double.parseDouble(textField.getText());
            double result = 0;

            switch (operator) {
                case "+":
                    result = num1 + num2;
                    break;
                case "-":
                    result = num1 - num2;
                    break;
                case "*":
                    result = num1 * num2;
                    break;
                case "/":
                    if (num2 != 0) {
                        result = num1 / num2;
                    } else {
                        textField.setText("Error");
                        return;
                    }
                    break;
            }

            textField.setText(String.valueOf(result));
            num1 = result;
            isOperatorClicked = true;
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new CalculadoraSi());
    }
}
