class MultiLineWriter:
    def __init__(self, output_file):
        self.output_file = output_file

    def start_writing(self):
        pass

    def start_writing(self):
        with open(self.output_file, "w") as file_handle:
            more_lines = True
            while more_lines:
                user_input = input("Enter line: ")
                file_handle.write(user_input + "\n")

                choice = input("Are there more lines y/n? ").lower()
                if choice != 'y':
                    more_lines = False
        print("Done! Lines have been saved.")