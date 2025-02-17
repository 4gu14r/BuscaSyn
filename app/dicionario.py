from nltk.corpus import wordnet as wn

def obter_sinonimos(palavra):
    sinonimos = set()
    for syn in wn.synsets(palavra, lang='por'):
        for lemma in syn.lemmas('por'):
            sinonimos.add(lemma.name())
    return sinonimos