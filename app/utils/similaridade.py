import sys
import os
import spacy

if getattr(sys, 'frozen', False):
    model_path = os.path.join(sys._MEIPASS, 'pt_core_news_lg')
    nlp = spacy.load(model_path)
else:
    nlp = spacy.load('pt_core_news_lg')
    

def similaridade(palavra, termo):
    doc_palavra = nlp(palavra)
    doc_termo = nlp(termo)
    
    if not doc_palavra.has_vector or not doc_termo.has_vector:
        return 0.0

    return doc_palavra.similarity(doc_termo)
