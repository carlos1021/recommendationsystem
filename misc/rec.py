from nltk.corpus import wordnet as wn
import nltk

#Helper function
def get_synonyms(word):
    synonyms = []
    for synsets in wn.synsets(word):
        for lemma in synsets.lemmas():
            #add ALL synonyms to list
            
            synonyms.append(lemma.name())
    #remove duplicate entries in our synonyms list
    synonyms = list(set(synonyms))
    try:
        synonyms.remove(word)
    except:
        print("")
    return synonyms


def recommend_synonym(word):
    synonyms = get_synonyms(word)
    if len(synonyms) > 0:
        print(f"Synonyms for '{word}':")
        for synonym in synonyms:
            print(synonym)
    else:
        print(f"No synonyms found for '{word}'.")
