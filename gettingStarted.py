def welcome_assignment_answers(question):

    if question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"

    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"

    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"

    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"

    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"

    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        answer = 5

    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        answer = 3

    elif question == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
        answer = "cf1d82a201ffd9b5fad5ba93aaeb77ce2293912d0c327a3a8c0b12c7a8e8cb17"

    elif question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        answer = "pcap"

    else:
        answer = "Error: question not recognized"

    return answer


if __name__ == "__main__":
    debug_question = "Are encoding and encryption the same? - Yes/No"
    print(welcome_assignment_answers(debug_question))
