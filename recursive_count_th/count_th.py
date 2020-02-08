'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
count = 0
def count_th(word):
    global count
    # create a base case
    if len(word) <= 1:
        return count
    else:
        if word[0] == 't' and word[1] == 'h':
            count += 1
            
            return count_th(word[2:])
        else:
            # recursive case
            return count_th(word[1:])
        
print(count_th('abcthefthghith'))