import spacy

nlp1 = spacy.load('en_core_web_sm')
nlp2 = spacy.load('en_core_web_md')

################ 1 ################

word1_1 = nlp1("cat")
word2_1 = nlp1("monkey")
word3_1 = nlp1("banana")

word1_2 = nlp2("cat")
word2_2 = nlp2("monkey")
word3_2 = nlp2("banana")

print(word1_1.similarity(word2_1), word1_2.similarity(word2_2))
print(word3_1.similarity(word2_1), word3_2.similarity(word2_2))
print(word3_1.similarity(word1_1), word3_2.similarity(word1_2))
print('\n')

################ 2 ################

tokens1 = nlp1('cat apple monkey banana ')
tokens2 = nlp2('cat apple monkey banana ')
for token1_1, token1_2 in zip(tokens1, tokens2):
    for token2_1, token2_2 in zip(tokens1, tokens2):
        print(token1_1.text, token2_1.text, token1_1.similarity(token2_1), token1_2.similarity(token2_2))

print('\n')

################ 3 ################

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence1 = nlp1(sentence_to_compare)
model_sentence2 = nlp2(sentence_to_compare)
for sentence in sentences:
    similarity1 = nlp1(sentence).similarity(model_sentence1)
    similarity2 = nlp2(sentence).similarity(model_sentence2)
    print(sentence + " - ", similarity1, " - ", similarity2)
print('\n')


########### Task1 ###########
# Write a note about what you found interesting about the similarities
# between cat, monkey and banana:

# 1. Cat and monkey seem to be similar because they are both animals

# 2. Similarly, banana and apple are similar because they are both fruits

# 3. Monkey and banana have a higher similarity than monkey and 
# apple. So we can assume that the model already puts together that
# monkeys eat bananas and that is why there is a significant similarity

# think of an example of your own:
word1 = nlp1("bus")
word2 = nlp1("bicycle")
word3 = nlp1("driver")

print(word1.similarity(word2)) # bus - bicycle
print(word3.similarity(word2)) # driver - bicycle (bicyclist)
print(word3.similarity(word1)) # driver - bus

########### Task2 ###########

# Run the example file with the simpler language model ‘en_core_web_sm’
# and write a note on what you notice is different from the model 'en_core_web_md'.


# The difference is in the accuracy of the predictions
# The output for "en_core_web_sm" and "en_core_web_md":
'''
0.5640838231302473 0.5351813232299611
0.5464804422621221 0.45207788279447625
0.6134374031915543 0.28154364860188125

cat cat 1.0 1.0
cat apple 0.42387104 0.28213844
cat monkey 0.44350967 0.5351813
cat banana 0.3863599 0.28154367
apple cat 0.42387104 0.28213844
apple apple 1.0 1.0
apple monkey 0.3563822 0.2929498
apple banana 0.48099723 0.5831844
monkey cat 0.44350967 0.5351813
monkey apple 0.3563822 0.2929498
monkey monkey 1.0 1.0
monkey banana 0.40807885 0.45207787
banana cat 0.3863599 0.28154367
banana apple 0.48099723 0.5831844
banana monkey 0.40807885 0.45207787
banana banana 1.0 1.0

where did my dog go -  0.4139478812332432  -  0.8794280609455339
Hello, there is my car -  0.559429350191411  -  0.8960133627039826
I've lost my car in my car -  0.6266647498198112  -  0.8872068799360076
I'd like my boat back -  0.32634652551717785  -  0.8219701705098686
I will name my dog Diana -  0.389808870191651  -  0.8207847990376582
'''