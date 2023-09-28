from nltk.corpus import wordnet as wn
import nltk

def get_synonyms(word):
    '''
    get_synonyms - gets all the synonyms for the word
    word - a word
    returns - a list of synonyms for word
    '''
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
    '''
    recommend_synonym - recommends synonyms based on the word
    word - a word
    returns - a list of recommended synonyms, removes duplicate entries
    '''
    synonyms = get_synonyms(word)
    if len(synonyms) > 0:
        #print(f"Synonyms for '{word}':")
        for synonym in synonyms:
            print(synonym)
    else:
        print(f"No synonyms found for '{word}'.")