def print_pattern(chars):
    #print(chars)
    total = ""
    start = 0
    end  = 1

    def print_back(word):
        total = ""
        if(len(word)==1):
            return total
        else:
            for i in word[len(word)-2::-1]:
                total += i
        return total


    reverseChar = chars[::-1]
    while end <= len(chars):
        newChars = reverseChar[start:end]
        total += ('.'.join(newChars + print_back(newChars))).center(len(chars)*4-3, '.')
        if(len(total) > 1):
            total += "\n"
        end +=1

    end -=1

    while end > 1:
        end -=1
        newChars = reverseChar[start:end]
        total += ('.'.join(newChars + print_back(newChars))).center(len(chars)*4-3, '.')
        if(end > 1):
            total += "\n"

    return total



arg = input()
print(print_pattern(arg))
