# Dependency (Uses-a)

class Printer:
    def print_page(self, text):
        print("Printing:", text)

class Report:
    def __init__(self, content):
        self.content = content

    def print_report(self, printer):
        # Temporary use of Printer
        printer.print_page(self.content)

# Run
my_printer = Printer()
my_report = Report("Q1 Results: Excellent!")
my_report.print_report(my_printer)
