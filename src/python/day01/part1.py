from pathlib import Path


class Solution:

    def __init__(self, position):
        self.position = position

    
    def find_password(self, input_file):

        with open(input_file, 'r') as file:
            lines = file.readlines()

        password = 0
        for line in lines:
            step = line.strip()

            if step.startswith('L'):
                self.position -= int(step[1:])

            elif step.startswith('R'):
                self.position += int(step[1:])

            # position is circular from 0 to 99

            self.position = self.position % 100

            if self.position == 0:
                password += 1

        
        return password
    
if __name__ == "__main__":
    solution = Solution(position=50)

    repo_root = Path(__file__).resolve().parents[3]
    input_path = repo_root / "data" / "day1" / "input.txt"

    result = solution.find_password(input_path)
    print(f"The password is: {result}")

