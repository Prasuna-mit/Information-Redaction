import nltk
import spacy
import argparse
import urllib
import re
import tempfile
import numpy
import glob
import regex as re
import os.path
import os
import pickle
import ntpath
import sys
import spacy
from commonregex import CommonRegex
from nltk.corpus import wordnet as wn
#from mosestokenizer import MosesTokenizer
from nltk.tokenize.treebank import TreebankWordDetokenizer
from copy import deepcopy
import spacy
#import en_core_web_sm
#from NLP import NLP

#nlp=en_core_web_sm.load()
nlp = spacy.load('en_core_web_sm')
#from spacy.lang.en import English

files_all = []
def read_arg(path):
    glob_files = glob.glob(path)
    for i in range(len(glob_files)):
        file = open(glob_files[i]).read()
        files_all.append(file)
        
    #print(files_all)    
    return files_all



# names

def san_names(file_read):
    san_names = []
    ncount = 0
    redacted_sentences = []
    for text in range(len(file_read)):
        doc = nlp(file_read[text])
        for ent in doc.ents:
            ent.merge()
        for token in doc:
            if token.ent_type_ == 'PERSON':
                redacted_sentences.append(" ████ ")
                ncount = ncount+1
            else:
                redacted_sentences.append(token.string)
        san_names.append("".join(redacted_sentences)) 
        
    return san_names,ncount

#dates

def red_dates(file_read1):
    rdates = []
    dcount = 0
    redacted_sentences1 = []
    for text1 in range(len(file_read1)):
        doc = nlp(file_read1[text1])
        for ent in doc.ents:
            ent.merge()
        for token in doc:
            if token.ent_type_ == 'DATE':
                redacted_sentences1.append(" ████ ")
                dcount = dcount+1
            else:
               redacted_sentences1.append(token.string)
        rdates.append("".join(redacted_sentences1))
        
         
    return rdates,dcount


#locations

def red_locations(file_read2):
    locs = []
    loc_count = 0
    redacted_sentences2 = []
    for text2 in range(len(file_read2)):
        doc = nlp(file_read2[text2])
        for ent in doc.ents:
            ent.merge()
        for token in doc:
            if token.ent_type_ == 'GPE':
                redacted_sentences2.append(" ████ ")
                loc_count = loc_count+1
            else:
               redacted_sentences2.append(token.string)
        locs.append("".join(redacted_sentences2))

    return locs,loc_count


#




#def names_red(files_all):
#    doc = nlp(files_all)
#    print("doc",doc)
#    redacted_sentences = []
#    for ent in doc.ents:
#        ent.merge()
#    for token in doc:
#        if token.ent_type_ == 'PERSON':
#            print(token.ent_type)
#            redacted_sentences.append(" ██ ")
#        else:
#            redacted_sentence.append(token.string)
#    return "".join(redacted_sentences)

#def red_names(ptext):
#    entity_names = []
#    final_file = []
#    total_data = ptext
#    for i in range(len(total_data)):
#        redaction_file = total_data[i]
#        sentences = nltk.sent_tokenize(redaction_file)
#        tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
#        tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
#        chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary = False)
#        for tree in chunked_sentences:
#            entity_names.extend(extract_entity_names(tree))
#        for e in entity_names:
#            redaction_file = redaction_file.replace(e,'██')
#            final_file.append(redaction_file)
#    return files_all
   



#def names_red(ptext):
 #   entity_names = []
 #   final_file = []
 #   total_data = ptext
 #   for i in range(len(files_all)):
 #       redaction_file = files_all[i]
 #       sentences = nltk.sent_tokenize(redaction_file)
  #      tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
   #     tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
   #     chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary = False)
   #     for tree in chunked_sentences:
   #         entity_names.extend(extract_entity_names(tree))
   #     for e in entity_names:
   #         redaction_file = redaction_file.replace(e,'██')
   #     final_file.append(redaction_file)
   # return final_file

       
