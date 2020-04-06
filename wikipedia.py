import argparse
import wikipedia

# python wikipedia_files.py --wiki "American Civil War"

# Download files from wikipedia for testing my project
def main(arguments):
    for wiki in arguments.wiki:
        wiki_ = wiki.replace(" ", "")
        file = 'demo_files/' + wiki_ + '.txt'
        f = open(file, 'a')
        f.write(wikipedia.page(wiki).content)
        f.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--wiki", action='append', type=str, required=True,
                        help="wikipedia titles")
    args = parser.parse_args()
    if args.wiki:
        main(args)
