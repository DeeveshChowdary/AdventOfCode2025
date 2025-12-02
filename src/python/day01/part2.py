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
            old_position = self.position

            if step.startswith('L'):
                move = -int(step[1:])
            elif step.startswith('R'):
                move = int(step[1:])
            else:
                continue  # skip invalid lines

            total_steps = abs(move)
            direction = 1 if move > 0 else -1

            for i in range(1, total_steps + 1):
                pos = (old_position + direction * i) % 100
                if pos == 0:
                    password += 1

            self.position = (self.position + move) % 100

        return password

if __name__ == "__main__":
    solution = Solution(position=50)

    repo_root = Path(__file__).resolve().parents[3]
    input_path = repo_root / "data" / "day1" / "input.txt"

    result = solution.find_password(input_path)
    print(f"The password is: {result}")