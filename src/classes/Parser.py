from collections import defaultdict
import re
from Utterance import Utterance

speaker_pattern = re.compile("[A-Z]{2,}:")


def parse_transcript(transcript_file):
    """
    :param transcript_file:
    :return speaker_transitions, character_utterances_map?:
    """
    with open(transcript_file) as f:
        lines = f.readlines()

    current_speaker = None
    speaker_transitions = defaultdict(defaultdict(str, int))

    all_utterances = []

    current_utterance = []
    for line in lines:
        skip_current = should_ignore(line)
        if skip_current:
            continue

        new_speaker = determine_speaker(line)
        if new_speaker:
            speaker_transitions[current_speaker][new_speaker.string] += 1
            current_speaker = disambiguate_speaker(new_speaker.string)
            all_utterances.append(Utterance(current_utterance, current_speaker))








def disambiguate_speaker(speaker):
    return speaker_dict.get(speaker, speaker)


def determine_speaker(line):
    speaker = speaker_pattern.match(line)
    if speaker:
        return speaker



def should_ignore(line):
    if line.strip() == "":
        return True

    if line[0] in ["(", "[", "{", "*"]:
        return True


    return False


def is_it_intro(line, intro_started):
    # figure out a way to reliably filter out intros. for now; ignore (i.e. accept) them
    return False


def tokenise(raw_string):

def parse_to_bag_of_words(tokenised_string):

