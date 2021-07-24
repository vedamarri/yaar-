import csv
name=input('name of the child?')
age=input('mention age')
dictionary = {'nameC': name,'ageC': age}
vedafile = open('info.csv', 'a')
writer= csv.writer(vedafile)
for i, dictionary[i] in dictionary.items():
    writer.writerrow([i],dictionary[i])
vedafile.close()

    

    



