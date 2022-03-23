def findDelimiters(x):
    #separating the total no. of delimiters given
    delimiters = set()
    i = 0    
    while i<len(x):
        delimiter=""
        if x[i]=='[':
            i+=1
            while x[i]!=']':
                delimiter+=x[i]
                i+=1
                
        delimiters.add(delimiter)
        i+=1
        
    return delimiters

def add(numbers):
    #base condition
    if numbers == "": return 0

    delimiters = set()
    delimiters.add(",")
    start_index = 0

    #setting delimiter and starting index
    if numbers[0][0:2]=="//":
        if numbers[0][2]!="[":
            delimiters = numbers[0][2:]
        else:
            delimiters = findDelimiters(numbers[0][2:])

        start_index = 1
        
if __name__ == "__main__":
    #taking infinite input
    numbers = []
    while 1:
        num = input()
        if num is "": break
        numbers.append(num)
    print(add(numbers))
