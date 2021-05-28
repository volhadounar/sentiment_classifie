def get_positive_words(file_name):
    positive_words = []
    try:
        with open(file_name) as pos_f:
            for lin in pos_f:
                if lin[0] != ';' and lin[0] != '\n':
                    positive_words.append(lin.strip())
    except IOError:
        pass
    return positive_words


def get_negative_words(file_name):
    negative_words = []
    try:
        with open(file_name) as pos_f:
            for lin in pos_f:
                if lin[0] != ';' and lin[0] != '\n':
                    negative_words.append(lin.strip())
    except IOError:
        pass    
    return negative_words


def strip_punctuation(s):
    punctuation_chars = ["'", '"', ',', '.', '!', ':', ';', '#', '@']
    for ch in punctuation_chars:
        s = s.replace(ch, '')
    return s


def get_neg(text, negative_words):
    cnt = 0
    for w in text.split():
        if strip_punctuation(w).lower() in negative_words:
            cnt += 1
    return cnt


def get_pos(text, positive_words):
    cnt = 0
    for w in text.split():
        if strip_punctuation(w).lower() in positive_words:
            cnt += 1
    return cnt


def read_source_file(file_name):
    res = []
    try:
        with open(file_name, 'r') as file:
            res = file.readlines()
    except IOError:
        pass
    return res


def calc_net_score(pos, neg):
    return (pos-neg)


def create_uploaded_file(from_file_name, upload_file_name,
                         positive_words, negative_words):
    lines = read_source_file(from_file_name)
    res_file = open(upload_file_name, 'w')
    res_file.write('Number of Retweets, Number of Replies, '+
                    'Positive Score, Negative Score, Net Score')
    res_file.write('\n')
    for line in lines[1:]:
        text, num_retweet, num_repl = line.strip().split(',')
        pos_score = get_pos(text, positive_words)
        neg_score = get_neg(text, negative_words)
        net = calc_net_score(pos_score, neg_score)
        row_data = '{}, {}, {}, {}, {}'.format(num_retweet, num_repl,
                                               pos_score, neg_score, net)
        res_file.write(row_data)
        res_file.write('\n')
    res_file.close()



