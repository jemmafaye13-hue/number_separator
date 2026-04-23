class NumberSeparator:
    def __init__(self, input_file):
        self.input_file = input_file
        self.even_file = "even.txt"
        self.odd_file = "odd.txt"

    def process_numbers(self):
        with open(self.input_file, 'r') as source_file:
            numbers = [int(line.strip()) for line in source_file if line.strip()]

        with (open(self.even_file, 'w') as even, open(self.odd_file, 'w') as odd):
            for num in numbers:
                if num % 2 == 0:
                    even.write(f"{num}\n")
                else:
                    odd.write(f"{num}\n")
