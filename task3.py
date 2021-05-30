import pymorphy2
import random
import itertools


morph = pymorphy2.MorphAnalyzer()

with open('rus_shuffled.txt', 'r', encoding='utf8') as f:
    noun = []
    adjf = []
    for line in f:
        wordlist = line.split()
        for word in wordlist:
            p = morph.parse(word)[0]
            pos = p.tag.POS
            if pos == 'NOUN':
                noun.append(p.normal_form)
            elif pos == 'ADJF':
                adjf.append(p.normal_form)


def get_combinations(noun, adjf):
    pairs = list(itertools.product(noun, adjf))
    random_choice = random.choice(pairs)
    yield random_choice


combinations = get_combinations(noun, adjf)
for i in combinations:
    print(i)

