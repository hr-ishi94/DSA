def word_frequency(sentence):
    words=sentence.split()
    freq={}

    for word in words:
        word=word.lower()
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
    return freq        

sentence="This is a simple example. This example demonstrates word frequency"
res=word_frequency(sentence)
print(res)