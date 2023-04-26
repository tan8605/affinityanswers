#its a function to rate the profanity of the tweet on the no of racial slurs
#slurs are in the other slurs.txt file 
def check_profanity(tweet, slur_set):
    # Remove non-alphanumeric characters and convert to lowercase
    tweet = re.sub(r'[^a-zA-Z0-9\s]', '', tweet).lower()
    # Split tweet into individual words
    words = tweet.split()
    # Count the number of slurs in the tweet
    num_slurs = sum(word in slur_set for word in words)
    # Determine the degree of profanity based on the number of slurs
    if num_slurs == 0:
        profanity = 'Clean'
    elif num_slurs == 1:
        profanity = 'Mild'
    elif num_slurs <= 3:
        profanity = 'Moderate'
    else:
        profanity = 'Severe'
    return profanity