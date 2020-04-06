import os
import re
import nltk
import glob
from nltk.tokenize import sent_tokenize
from nltk.tag.stanford import StanfordNERTagger
import sys
import pprint
from dateparser.search import search_dates
from nltk.corpus import wordnet


# Takes arguments from terminal; Downloads nltk files; controls stats; collects all files using glob; cleans the files;
def clean_files(arguments):
    final_stats = dict()
    download_nltk_stuff()
    for _input in arguments.input:
        for file in glob.glob(_input):  # clean every file in the input glob
            print(file)
            with open(file, 'r') as f:
                dirty_string = f.read()
            clean_string, stats = process_file_flags(dirty_string, arguments)
            final_stats[file] = stats
            write_redacted_file(file, clean_string, arguments.output)
    if arguments.stats:  # if stats is on, write the stats
        write_stats(final_stats, arguments.stats)


# These are nltk models necessary to run the program
def download_nltk_stuff():
    nltk.download('averaged_perceptron_tagger')
    nltk.download('punkt')


# Process the file flags (name, gender, date, concept)
def process_file_flags(dirty_string, arguments):
    cleaned_string = dirty_string
    stats = dict()
    if arguments.names:
        cleaned_string, stat = redact_names(cleaned_string)
        stats['Name'] = stat
    if arguments.genders:
        cleaned_string, stat = redact_genders(cleaned_string)
        stats['Gender'] = stat
    if arguments.dates:
        cleaned_string, stat = redact_dates(cleaned_string)
        stats['Date'] = stat
    if arguments.concept:
        concept_stats = dict()
        for concept in arguments.concept:
            cleaned_string, stat = redact_concepts(cleaned_string, concept)
            concept_stats[concept] = stat
        stats['Concept'] = concept_stats
    return cleaned_string, stats


# Redacts all names from the file using StanfordNERTagger
def redact_names(old_string):
    REDACTED_NAME = '[REDACTED NAME]'
    new_string = old_string
    stats = dict()
    java_path = 'stanford-ner/stanford-ner-2018-10-16/java.exe'  # included in the files
    os.environ['JAVAHOME'] = java_path  # necessary to find java path for the stanford model

    # stanford model
    stanford = StanfordNERTagger('stanford-ner/english.all.3class.distsim.crf.ser.gz',
                                 'stanford-ner/stanford-ner-2018-10-16/stanford-ner-3.9.2.jar')

    words = nltk.word_tokenize(new_string)  # tokenize words from the string
    tags = stanford.tag(words)
    for tag in tags:
        if tag[1] == 'PERSON':  # if the entity is a person, redact it
            new_string = new_string.replace(tag[0], REDACTED_NAME, 1)
            if tag[0] in stats.keys():  # keep stats
                stats[tag[0]] = stats.get(tag[0]) + 1
            else:
                stats[tag[0]] = 1

    return new_string, stats


# Redact all genders and gendered words from the file
def redact_genders(old_string):
    REDACTED_GENDER = ' [REDACTED GENDER] '
    new_string = old_string
    stats = dict()

    with open('gendered_words.txt', 'r') as f:  # using a list of gendered words to redact
        for line in f:
            if line[0] is not '#':
                line = line.replace('\n', '')
                _line = line
                line = ' ' + line + ' '
                gendered_line = re.compile(line, re.IGNORECASE)
                new_string = gendered_line.subn(REDACTED_GENDER, new_string)
                if new_string[1] > 0:
                    stats[_line] = new_string[1]
                new_string = new_string[0]

    return new_string, stats


# Redact all dates from the file
def redact_dates(old_string):
    REDACTED_DATE = '[REDACTED DATE]'
    new_string = old_string
    stats = dict()

    date_instances = search_dates(new_string)  # from dateparser.search
    for date in date_instances:
        new_string = new_string.replace(date[0], REDACTED_DATE)
        if date[0] in stats.keys():
            stats[date[0]] = stats.get(date[0]) + 1
        else:
            stats[date[0]] = 1

    return new_string, stats


# Redact a specified concept
def redact_concepts(old_string, concept):
    REDACTED_CONCEPT = '[REDACTED CONCEPT]'
    new_string = old_string
    stats = dict()
    concept_synonyms = list()

    for synonym in wordnet.synsets(concept):
        for item in synonym.lemmas():
            concept_synonyms.append(item.name())

    concept_synonyms = set(concept_synonyms)  # remove duplicates

    sentences = sent_tokenize(new_string)
    for word in concept_synonyms:
        word = word.replace('_', ' ')
        word = ' ' + word + ' '  # don't want to remove words that just contain this word as a sub-component
        word = word.lower()
        for sentence in sentences:
            if word in sentence.lower():
                new_string = new_string.replace(sentence, REDACTED_CONCEPT)
                if word[1:-1] in stats.keys():
                    stats[word[1:-1]] = stats.get(word[1:-1]) + 1
                else:
                    stats[word[1:-1]] = 1
    return new_string, stats


# write the redacted file with new name to directory specified
def write_redacted_file(file_name, clean_string, directory):
    if '/' in file_name:  # if file location is not in cwd
        new_file_name = file_name[file_name.rfind('/'):]
        new_file_name = new_file_name + '.redacted'
    elif '\\' in file_name:  # if file location is not in cwd
        new_file_name = file_name[file_name.rfind('\\'):]
        new_file_name = new_file_name + '.redacted'
    else:  # if file location is in cwd
        new_file_name = file_name + '.redacted'

    write_location = directory + new_file_name
    write_location = write_location.replace("'", "")

    if os.path.exists(write_location):
        os.remove(write_location)

    with open(write_location, 'a') as output:
        output.write(clean_string)


# Write the stats to stderr, stdout, or a file
def write_stats(stats, output):
    if output.lower() == 'stderr':
        sys.stderr.write(pprint.pformat(stats))
    if output.lower() == 'stdout':
        pprint.pprint(stats)
    else:
        with open(output, 'a') as output:
            output.write(pprint.pformat(stats))
