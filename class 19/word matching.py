def word_count(word_list):
    count=0
    for word in word_list:
        if word[0] == word[-1]:
            count +=1
    print("the word matching first and last character are ",count)

word_list = ["civic","acaia","mom","play","run","clip","race car"]
word_count(word_list)
