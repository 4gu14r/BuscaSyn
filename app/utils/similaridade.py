import spacy

nlp = spacy.load('pt_core_news_md')

def similaridade(palavra, termo):
    
    doc_palavra = nlp(palavra)
    doc_termo = nlp(termo)

    return doc_palavra.similarity(doc_termo)
