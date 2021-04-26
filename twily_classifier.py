from textblob.classifiers import NaiveBayesClassifier

import pandas as pd
import numpy as np

def trainer():
    train = [
        ("i am good", "pos"),
        ("fine thanks", "pos"),
        ("i feel really good!", "pos"),
        ("doing well", "pos"),
        ("thank you", "pos"),
        ("i am crappy", "neg"),
        ("yay", "pos"),
        ("wtf", "neg"),
        ("no thanks", "pos"),
        ("today was fantastic", "pos"),
        ("not good", "neg"),
        ("it was so nice", "pos"),
        ("i don't know", "neg"),
        ("asshole", "neg"),
        ("fucker", "neg"),
        ("i hate it here", "neg"),
        ("screw you", "neg"),
        ("it was peaceful", "pos"),
        ("fuck you", "neg"),
        ("i can't live like this", "neg"),
        ("im smiling", "pos"),
        ("sad", "neg"),
        ("big moves", "pos"),
        ("get me a rep", "neg"),
        ("they're kind", "pos"),
        ("this is crap", "neg"),
        ("contact us", "pos"),
        ("this was great", "pos"),
        ("no", "neg"),
        ("no", "neg"),
        ("fuck yeah", "pos"),
        ("is that so", "neg"),
        ("you suck", "neg"),
        ("yes", "pos"),
        ("this is not working", "neg")
            ]

    return NaiveBayesClassifier(train)


if __name__ == "__main__":
    user_input = "I'm so happy"
    classy = trainer().prob_classify(user_input)
    print()
    print(f'String:  {user_input}')
    print(f'---------{len(user_input) * "-"}+')
    print(f'Negative probability: {classy.prob("neg")}')
    print(f'Positive probability: {classy.prob("pos")}')
