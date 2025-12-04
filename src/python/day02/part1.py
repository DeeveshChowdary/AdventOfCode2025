from pathlib import Path


class Solution:

    def __init__(self):
        self.total = 0


    def find_sum(self, input_file):

        with open(input_file, 'r') as file:
            lines = file.readlines()

        ranges = []
        for line in lines:
            number = line.strip().split(',')
            ranges.extend(number)
        
        # print(ranges)

        int_ranges = []

        for r in ranges:
            start, end = map(int, r.split('-'))
            int_ranges.append((start, end))

        int_ranges.sort(key=lambda x: x[0])

        for start, end in int_ranges:
            if len(str(start)) % 2 == 0 or len(str(end)) % 2 == 0:
                for i in range(start, end + 1):
                    str_i = str(i)
                    mid = len(str_i) // 2
                    if str_i[:mid] == str_i[mid:]:
                        self.total += i
            else:
                pass


        return self.total


    
if __name__ == "__main__":
    solution = Solution()

    repo_root = Path(__file__).resolve().parents[3]
    input_path = repo_root / "data" / "day2" / "input.txt"

    result = solution.find_sum(input_path)
    print(f"The total sum is: {result}")

