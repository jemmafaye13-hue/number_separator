class NumberSeparator:
    def __init__(self, input_file):
        self.input_file = input_file
        self.even_file = "even.txt"
        self.odd_file = "odd.txt"
        
    def process_numbers(self):
        with open(self.input_file, 'r') as f:
            numbers = [int(line.strip()) for line in f if line.strip()]

        with open(self.even_file, 'w') as ev, open(self.odd_file, 'w') as od:
            for num in numbers:
                if num % 2 == 0:
                    ev.write(f"{num}\n")
                else:
                    od.write(f"{num}\n")
