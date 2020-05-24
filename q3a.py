fileHandler = open('file.txt','r') #open file for reading
text = ""
for line in fileHandler.readlines():
    text += line #read all lines to textstring
fileHandler.close()

pattern = input("Enter code")
length_of_data1 = len(text)
length_of_data2 = len(pattern)
i = length_of_data1 - length_of_data2; #get difference in lengths b/w text and pattern

index = 0;
for x in range(0,i+1): #starting index to check
    d2 = 0
    if text[0:pattern.__len__()] == pattern: #check current 3 first characters of text string
         print("found at index", x) #print index where the pattern matched
    text = text[1:] #delete first character of string text everytime





