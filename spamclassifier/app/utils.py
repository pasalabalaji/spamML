import pickle

vectorizer=pickle.load(open("vectorizer.pkl","rb"))
model=pickle.load(open("model.pkl","rb"))




import nltk
from nltk.corpus import stopwords
stopwords.words('english')
import string
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()

def transform(text):
    text=text.lower()
    text=nltk.word_tokenize(text)
    res=[]
    for i in text:
        if i.isalnum():
           res.append(i)
    text=res[:]
    res.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            i=ps.stem(i)
            res.append(i)
    return " ".join(res)

def classify(sms):
    ttext=transform(sms)
    X=vectorizer.transform([ttext]).toarray()
    res=model.predict(X)
    return res