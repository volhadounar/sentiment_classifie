from sentiment_classifie import (get_positive_words,
                                 get_negative_words,
                                 create_uploaded_file
                                )

if __name__== '__main__':   
    positive_words = get_positive_words('positive_words.txt')
    negative_words = get_negative_words('negative_words.txt')
    create_uploaded_file('project_twitter_data.csv', 'resulting_data.csv',
                         positive_words, negative_words)