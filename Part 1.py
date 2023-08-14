#You will write code to create a csv file called resulting_data.csv, which contains the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall) for each tweet. The file should have those headers in that order. 

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(word):
    for punct in punctuation_chars:
        word = word.replace(punct, "")
    return word

def get_neg(sentences):
    sentences = strip_punctuation(sentences.lower())
    list_sentences = sentences.split()
    
    count = 0
    for word in list_sentences:
        if word in negative_words:
            count += 1
    return count

def get_pos(sentences):
    sentences = strip_punctuation(sentences.lower())
    list_sentences = sentences.split()
    
    count = 0
    for word in list_sentences:
        for pos_word in positive_words:
            if word == pos_word:
                count += 1
    return count


file = open("project_twitter_data.csv", "r")
data = file.readlines()

reader = file.read()
negative = positive = 0

for i in reader:
    negative += get_neg(i)
    positive = get_pos(i)

negative_string = str(negative)
positive_string = str(positive)

net_value = positive + negative
net_string = str(net_value)

result = open("resulting_data.csv", "w")

result.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")

for i in data[1:]:
    res_row = ""
    splitted = i.strip().split(",")
    
    res_row = ("{},{},{},{},{}".format(splitted[1], splitted[2], get_pos(splitted[0]), get_neg(splitted[0]), (get_pos(splitted[0]) - get_neg(splitted[0]))))
    result.write(res_row + "\n")
    
result.close()
