from main import main
import argparse


# Test Redact Names
def test_names():
    try:
        parser = argparse.ArgumentParser()
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
        args = parser.parse_args(["--input", "demo_files/JimWalmsley.txt",
                                  "--output", "demo_files_redacted/",
                                  "--names"])
        main(args)

        redacted = open("demo_files_redacted/JimWalmsley.txt.redacted", "r").read()
        redacted_test = open("demo_test_files/names_test", "r").read()
        assert redacted == redacted_test
        print("passed test names")
    except AssertionError:
        print("failed test names")


# Test Redact Genders
def test_genders():
    try:
        parser = argparse.ArgumentParser()
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
        args = parser.parse_args(["--input", "demo_files/JimWalmsley.txt",
                                  "--output", "demo_files_redacted/",
                                  "--genders"])
        main(args)

        redacted = open("demo_files_redacted/JimWalmsley.txt.redacted", "r").read()
        redacted_test = open("demo_test_files/genders_test.txt", "r").read()
        assert redacted == redacted_test
        print("passed test genders")
    except AssertionError:
        print("failed test genders")


# Test Redact Dates
def test_dates():
    try:
        parser = argparse.ArgumentParser()
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
        args = parser.parse_args(["--input", "demo_files/JimWalmsley.txt",
                                  "--output", "demo_files_redacted/",
                                  "--dates"])
        main(args)

        redacted = open("demo_files_redacted/JimWalmsley.txt.redacted", "r").read()
        redacted_test = open("demo_test_files/dates_test.txt", "r").read()
        assert redacted == redacted_test
        print("passed test dates")
    except AssertionError:
        print("failed test dates")


# Test Redact Concepts
def test_concepts():
    try:
        parser = argparse.ArgumentParser()
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
        args = parser.parse_args(["--input", "demo_files/JimWalmsley.txt",
                                  "--output", "demo_files_redacted/",
                                  "--concept", "state"])
        main(args)

        redacted = open("demo_files_redacted/JimWalmsley.txt.redacted", "r").read()
        redacted_test = open("demo_test_files/concepts_test.txt", "r").read()
        assert redacted == redacted_test
        print("passed test concept")
    except AssertionError:
        print("failed test concept")


if __name__ == '__main__':
    test_names()
    test_genders()
    test_dates()
    test_concepts()
