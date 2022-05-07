'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

x = "mississippi"

letter = {} 

for keys in x: 
    letter[keys] = letter.get(keys, 0) + 1
  
print (str(letter))

