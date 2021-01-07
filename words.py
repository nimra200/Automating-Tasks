import requests

def print_result(response, output):
    """ Response: the response to a request made to the API
    Prints out the words resulting from the request.
    """
    print(output) # an explanation of the results to the user 
    for result in response.json():
        print(result["word"])

def user_prompt():
    input_word = input ("Which word do you want to learn more about? ")
    parameter = {"rel_trg": input_word, "max": 5}
    # request for at most 5 words that are associated with input_word 
    response = requests.get('https://api.datamuse.com/words',parameter)
    print_result(response, "The word '" + input_word + "' is associated with:" )
    checkNoun(input_word)

def checkNoun(word):
    ans = input ("Is this word a noun? Press y/n. ")
    while not (ans == 'y' or ans == 'n'):
        ans = input ("Please enter a valid input. ")

    if ans == 'y':
        parameter = {"rel_jjb": word, "max": 5}
         # request for most common adjectives
        response = requests.get('https://api.datamuse.com/words',parameter)
        print_result(response, "Popular adjectives for this noun are: ")
    
    else:
        print("End of program.\n")


if __name__ == "__main__": 
    user_prompt()

