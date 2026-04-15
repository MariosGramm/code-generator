from argparse import ArgumentParser
from code_gen import generate_code as code_generation
from code_gen import save_code

def generate_code(description: str, with_tests: bool = False, filename: str = None):
    code, tests = code_generation(description)

    if filename:
        save_code(code, filename)
    
    if with_tests:
        return code, tests
    else:
        return code, None
    
def interactive_mode():
    while True:
        description = input("Please provide a code description")

        if description:
            description.strip()
        else:
            print("Code decription is empty. Please try again.")
            print("")
            continue
        
        
        with_tests_input = ""
        
        while True:
            with_tests_input = input("Would you like tests to be generated?(y/n)")

            if with_tests_input:
                with_tests_input.strip()
            if with_tests_input.lower() == "y":
                with_tests = True
                break
            elif with_tests_input.lower() == "n":
                with_tests = False
                break
            print("Please provide a valid answer (y/n) or (Y/N)")
        
        while True:
            print("Please provide a filename for the code to be saved at.")
            print("If you don't want the code to be saved, just continue by pressing enter.")

            filename = input("Filename: ")

            if filename:
                filename.strip()

            for char in ['\\', '/', ':', '*', '?', '"', '<', '>', '|']:
                if char in filename:
                    print(f"Filename containts a forbidden character: '{char}'")
                    print("Please try again. File cannot be saved.")
                    print("")
                    continue

            break

        generate_code(description, with_tests, filename)

    

