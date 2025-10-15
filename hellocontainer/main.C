#include <iostream>
#include <string>

int main(int argc, char **argv) {
  std::string choice = "";
  std::cout << "Hello container" << std::endl;
  
  while(choice != "quit") {
	std::cout << "Enter your choice:";
	std::cin >> choice;
	std::cout << "You chose: " << choice << std::endl;
  }
  return 0;

}
