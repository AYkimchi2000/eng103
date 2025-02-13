def word_length_std_dev(text):
    '''
    Calculates the sample standard deviation of word lengths in a given text.
    Args:
        text (str): A string of words separated by spaces.
    Returns:
        float: The sample standard deviation of the lengths of words in the text.
    '''
    word_list = text.split()
    word_lengths = [len(word) for word in word_list]
    mean = sum(word_lengths) / len(word_lengths)
    sum_squared_diffs = sum((length - mean) ** 2 for length in word_lengths)
    variance = sum_squared_diffs / (len(word_lengths) - 1)
    standard_deviation = (variance) ** 0.5
    return standard_deviation

