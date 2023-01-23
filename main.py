from textblob import TextBlob
words=['data wrds']

corrected_word =[]
for i in words:
    corrected_word.append(TextBlob(i))
print('Wrong words :' , words)
print('Corrected Words are : ')

for i in corrected_word:
    print(i.correct(), end=' ')
    
    