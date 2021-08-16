import pandas as pd
data=pd.read_csv('t8.shakespeare.txt',header=None,delimiter="\n")
word=pd.read_csv('find_words.txt',header=None,delimiter="\n")
dictionary=pd.read_csv('french_dictionary.csv',header=None)
data.to_csv('output.csv',na_rep='(missing)')
output=pd.read_csv('output.csv',header=None)
output=output[1][194:500] #tested for 500 words
output=list(output)
for i in range(len(output)):
    output[i]=output[i].split()
for i in range(len(output)):
    for j in range(len(output[i])):
        for k in range(len(dictionary)):
            if (output[i][j] == dictionary[0][k]):
                output[i][j]=dictionary[1][k]
output2=[]
for i in output:
    output2.append(' '.join(i))
textfile=open('file.txt','w')
for i in output2:
    textfile.write(i+'\n')
textfile.close()
