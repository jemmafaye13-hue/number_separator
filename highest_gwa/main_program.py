class GWAAnalyzer:
    def __init__(self, input_filename):
        self.input_filename = input_filename

    def find_highest_gwa(self):
        try:
            with open(self.input_filename, mode='r') as gwa_records:
                top_student_name = None
                highest_gwa_value = 5.0

            for line in gwa_records:
                if line.strip():
                name, gwa = line.strip().split(',')
                if float(gwa) < highest_gwa_value:
                    highest_gwa_value = float(gwa)
                    top_student_name = name