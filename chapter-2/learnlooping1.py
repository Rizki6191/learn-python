w = input("Enter any word: ")

for i in range(1, len(w) + 1):
    print(w[:i])  

for i in range(len(w) - 1, 0, -1):
    print(w[:i])  
