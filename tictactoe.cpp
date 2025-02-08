#include <iostream>
#include <cctype> // For isdigit function

int main() {
    int height;
    bool validInput = false;

    // Loop until a valid integer is entered
    while (!validInput) {
        std::cout << "Enter the height of your pyramid: ";
        std::string input;
        std::getline(std::cin, input);

        // Check if all characters in the input are digits
        validInput = true;
        for (char ch : input) {
            if (!isdigit(ch)) {
                validInput = false;
                break;
            }
        }

        if (validInput) {
            height = std::stoi(input); // Convert the string to an integer
        } else {
            std::cout << "Invalid input! Please enter an integer." << std::endl;
        }
    }

    int side_space = 0;

    // Loop to print the pyramid
    for (int i = 0; i < height / 2; ++i) {
        // Print leading spaces
        for (int j = 0; j < side_space; ++j) {
            std::cout << " ";
        }

        // Print stars
        for (int j = 0; j < height - 2 * i; ++j) {
            std::cout << "*";
        }

        std::cout << std::endl;
        side_space += 1;
    }

    return 0;
}
