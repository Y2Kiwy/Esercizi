def anagram_checker(string1: str, string2: str) -> bool:

    '''
    Can compare if two strings are anagrams of each other excluding non-alphabetic characters

    Args:
        string1: str -> The first string to compare
        string2: str -> The second string to compare

    Retrun:
        True: bool -> If the strings are anagrams of each other
        False: bool -> If the strings are not anagrams of each other
    '''
    
    # Remove envery non alphabetic character in the string and lower the entire string
    string1_list: list = list(filter(str.isalpha, string1.lower()))
    string2_list: list = list(filter(str.isalpha, string2.lower()))

    # Sort the remain characters by alphabetic order
    string1_list.sort()
    string2_list.sort()

    # Check if the length of the two string corrispond
    if len(string1_list) != len(string2_list):
        return False
    else:
        # Compare each alphabetic character of the string
        for index in range(len(string1_list)):
            if string1_list[index] != string2_list[index]:
                return False
        
        return True

    