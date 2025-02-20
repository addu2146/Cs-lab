mystr = "he"
if(len(mystr)<2):
   print("The string should be at least two characters long\n")
else:
   newstr=mystr[:2]+mystr[-2:]
print(newstr)
