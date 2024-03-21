import os

#made by haribv

def scan_file(file_path, search_terms):
    found_viruses = []  # List to store found viruses in the file
    try:
        with open(file_path, 'r', encoding='latin1') as file:
            lines = file.readlines()
            for line_number, line in enumerate(lines):
                for term in search_terms:
                    if term.lower() in line.lower():
                        found_viruses.append((term, line_number + 1))  # Store found virus and its line number
        if found_viruses:
            print(f"{file_path}: Viruses found:")
            with open("virus.txt", "a") as virus_file:
                for virus, line_number in found_viruses:
                    print(f"- '{virus}' in line {line_number}")
                    virus_file.write(f"{file_path}: Virus found - '{virus}' in line {line_number}\n")
        else:
            print(f"{file_path}: No viruses found")
    except FileNotFoundError:
        print("Error: The specified file does not exist.")

if __name__ == "__main__":
    file_path = input("Enter the path of the file to check: ")
    search_terms = input("Enter search terms (comma-separated): ").split(",")
    
    if os.path.exists(file_path):
        scan_file(file_path, search_terms)
    else:
        print("Error: The specified file does not exist.")
