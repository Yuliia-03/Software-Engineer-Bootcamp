# === Your task ==============================================================
# Let's have some 'fun'.
# Go to http://en.wikipedia.org/wiki/Garden_path_sentence and have a brief read 
# at what a 'Garden Path sentence' is (at the top) and look at the 'Examples'

# Create the file garden.py for this task.
# 1. Use some Garden Path sentences or think up your own (at least 5).
# 2. Tokenise and perform Entity recognition for each of the sentences 
#    after you have stored them in a list called gardenpathSentences.
# 3. See how spaCy has categorised these sentences and look up the entities you
#    don't understand
# 4. At the bottom of your file, write a comment about two unusual entities 
# you found that spaCy gave one of the words of your sentences - did you expect this?

import spacy

nlp = spacy.load('en_core_web_sm')

# stores sentences in a list called gardenpathSentences
gardenpathSentences = [
    'Mary gave the child the dog bit a Band-Aid.', 
    'When Fred eats food gets thrown', 
    'Helen is expecting tomorrow to be a bad day.',
    'The cotton clothing is made of grows in Mississippi.',
    'After Bill drank the water proved to be poisoned.',
    'The tycoon, sold the offshore oil tracts for a lot of money, wanted to kill JR.']


doc = [nlp(sentence) for sentence in gardenpathSentences]

for sentence in doc:

    # Tokenises for each of the sentences 
    print([token.orth_ for token in sentence if not token.is_punct | token.is_space])

    # performs Entity recognition for each of the sentences
    print([(i, i.label_, i.label) for i in sentence.ents],'\n')


# 1. a bad day - 'DATE'
#    a bad day - it is a characteristic of the day, not a specific date

# 2. JR - 'ORG'
#    JR - JR is the pseudonym of a French photographer and street artist.
#         It should be 'PERSON', not 'ORG'