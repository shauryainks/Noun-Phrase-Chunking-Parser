import nltk

import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> SF Conj SF | SF | SF SF
SF -> PH V | PH V PH | V PH | PH PH | PH Conj
PH -> P NP | P NP P | NP P | NP | P NP N | NP P NP
NP -> N | Det N | Det AD N | P Det AD | AD N | P Det AD N | V N P | AD N
AD -> Adj | Adj Adj | Adj Adj Adj | Adj Adj Adj Adj

"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    sentence_list = [word for word in nltk.tokenize.word_tokenize(
        (sentence.lower())) if any(char.isalpha() for char in word)]
    return sentence_list


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    # recursive algo
    list_of_nouns = []

    # if it is a str, that means it is empty or the last one
    if type(tree) == str:
        return []

    # if len(tree) == 0 and tree.label() == NP -> it means, it doesn't have any children which means we have reached the end of the tree
    if len(tree) == 0 and tree.label() == 'NP':
        return [tree]

    # if tree is empty
    # if no children - this is the final, move ahead recursively
    if len(tree) == 0:
        return []

    # main loop to call np_chunk function recursively, to see if any children have any values that are worth saving
    for leaf in tree:
        # add to the list if it is valuable
        list_of_nouns += np_chunk(leaf)
    # if len of list_of_nouns = 0 and tree.label() == 'NP' we are at the end just return the tree
    if len(list_of_nouns) == 0 and tree.label() == 'NP':
        return [tree]
    return list_of_nouns


if __name__ == "__main__":
    main()
