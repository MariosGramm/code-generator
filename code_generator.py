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

    print("""
============================================================================================
||                                                                                        ||
||   ██████╗ ██████╗ ██████╗ ███████╗                                                     ||
||  ██╔════╝██╔═══██╗██╔══██╗██╔════╝                                                     ||
||  ██║     ██║   ██║██║  ██║█████╗                                                       ||
||  ██║     ██║   ██║██║  ██║██╔══╝                                                       ||
||  ╚██████╗╚██████╔╝██████╔╝███████╗                                                     ||
||   ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝                                                     ||
||                                                                                        ||
||   ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗          ||
||  ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗         ||
||  ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝         ||
||  ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗         ||
||  ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║         ||
||   ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝         ||
||                                                                                        ||
============================================================================================
""")

    print("")
    print("Welcome to the code generator!")


    while True:
        print("")
        description = input("Please provide a code description: ")

        if description:
            description = description.strip()
        else:
            print("Code decription is empty. Please try again.")
            print("")
            continue
        
        
        with_tests_input = ""
        
        while True:
            with_tests_input = input("Would you like tests to be generated?(y/n): ")

            if with_tests_input:
                with_tests_input = with_tests_input.strip()
            if with_tests_input.lower() == "y":
                with_tests = True
                break
            elif with_tests_input.lower() == "n":
                with_tests = False
                break
            print("")
            print("Please provide a valid answer (y/n) or (Y/N)")
        
        while True:
            print("")
            print("Please provide a filename for the code to be saved at.")
            print("If you don't want the code to be saved, just continue by pressing enter.")
            print("")

            filename = input("Filename: ")

            if filename:
                filename = filename.strip()
            else:
                break

            forbidden_character_found = False
            for char in ['\\', '/', ':', '*', '?', '"', '<', '>', '|']:
                if char in filename:
                    print(f"Filename containts a forbidden character: '{char}'")
                    print("Please try again. File cannot be saved.")
                    forbidden_character_found = True
                    break
            
            if forbidden_character_found:
                continue
            else:
                break

        code, tests = generate_code(description, with_tests, filename)

        print("\n-- Generated Code --\n")
        print(code)

        if tests:
            print("\n-- Generated Tests --\n")
            print(tests)

        while True:
            print("")
            again = input("Would you like to continue generating code? (y/n): ")

            if again:
                again = again.strip().lower()
            if again.startswith("y"):
                break
            elif again.startswith("n"):
                print("Exit...")
                return
            else:
                print("")
                print("Please provide a valid answer (y/n) or (Y/N)")
        

def main():
    parser = ArgumentParser(prog= "Python Code Generator",
                            description= "Python Code Generator from natural language")
    parser.add_argument("description", nargs="?", help="Short description of the code that will be generated")
    parser.add_argument("--with-tests", action="store_true", help= "Generate tests for the generated code")
    parser.add_argument("--save", metavar= "FILE", help= "Filename to save the generated code")
    parser.add_argument("-i", "--interactive", action= "store_true", help= "Run in interactive mode")

    args = parser.parse_args()

    if args.interactive or not args.description:
        interactive_mode()
        return 
    
    code, tests = generate_code(
        description= args.description,
        with_tests = args.with_tests,
        filename= args.save
    )

    print("\n-- Generated Code --\n")
    print(code)

    if args.with_tests and tests:
        print("\n-- Generated Tests --\n")
        print(tests)



if __name__ == "__main__":
    main()