# A file that contains functions for analysing the text

def count_words(text):
    """
    Counts the number of words in a given text.
    
    Args:
        text (str): The text to count words in.
        
    Returns:
        print({num_words}): The number of words in the text.
    """
    num_words = len(text.split())
    return num_words

def count_chars(text):
    """
    Counts the number of times each character appears in the text.

    Args:
        text (str): The text to count characters in, all converted to lowercase.
    
    Returns:
        chars {str:int}: A dictionary of counts of each unique character in the text.
    """
    chars = {}
    lowercase_text = text.lower()

    for i in lowercase_text:
        if i not in chars:
            chars[i] = 1
        else:
            chars[i] += 1
    return chars

def sorted_chars(char_count):
    """
    Orders counts of characters from the text file from greatest to least.

    Args:
        char_count {str:int}: A dictionary of the occurence of each unique character in the text.

    Returns:
        [{}]: A sorted list of dictionaries, each corresponding to one character and its count.
    """        
    char_list =[]
    for i in char_count:
        i_dict = {}
        i_dict["char"] = i
        i_dict["num"] = char_count[i]
        char_list.append(i_dict)

    def get_num(char_dict):
        return char_dict["num"]

    char_list.sort(key=get_num, reverse=True)

    return char_list



