// This calculator was coded by Sami Elsayed

# include <iostream>
using namespace std;

int calculator() {
  char op;
  float num1, num2;

  cout << "Enter operator: (+), (-), (*), (/): ";
  cin >> op;

  cout << "Enter two operands: ";
  cin >> num1 >> num2;

  switch(op) {

    case '+':
      cout << num1 << " + " << num2 << " = " << num1 + num2;
      break;

    case '-':
      cout << num1 << " - " << num2 << " = " << num1 - num2;
      break;

    case '*':
      cout << num1 << " * " << num2 << " = " << num1 * num2;
      break;

    case '/':
      cout << num1 << " / " << num2 << " = " << num1 / num2;
      break;

    default:
      cout << "Invalid Operator!";
      break;
  }

  return 0;
}
