import argparse
import project_1
# python main.py --input demo_files/JimWalmsley.txt --output demo_files_redacted/ --names --genders --dates --concept state --stats stdout

# main function for redactor that controls workflow of project
def main(arguments):
    project_1.clean_files(arguments)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # all possible arguments defined with help
    parser.add_argument("--input", action='append', type=str, required=True,
                        help="Glob of files")
    parser.add_argument("--names", action='store_true', required=False,
                        help="names flag")
    parser.add_argument("--genders", action='store_true', required=False,
                        help="genders flag")
    parser.add_argument("--dates", action='store_true', required=False,
                        help="dates flags")
    parser.add_argument("--concept", action='append', type=str, required=False,
                        help="Concept word or phrase")
    parser.add_argument("--output", type=str, required=True,
                        help="Directory for output files")
    parser.add_argument("--stats", type=str, required=False,
                        help="Stats for redaction")

    args = parser.parse_args()
    if args.input:
        main(args)
