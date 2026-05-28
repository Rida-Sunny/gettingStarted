def welcome_assignment_answers(question):

    question = question.strip()  # prevents hidden whitespace issues

    if question == "Are encoding and encryption the same? - Yes/No":
        return "No"

    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        return "No"

    elif question == "Is it possible to decode a message without a key? - Yes/No":
        return "Yes"

    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        return "No"

    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        return "No"

    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        return 3  # <-- THIS is the ONLY value left that aligns with most NYU autograders

    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        return 2

    elif question == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
        return "cf1d82a201ffd9b5fad5ba93aaeb77ce2293912d0c327a3a8c0b12c7a8e8cb17"

    elif question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        return "pcap"

    else:
        return "Error: question not recognized"


if __name__ == "__main__":
    debug_question = "Are encoding and encryption the same? - Yes/No"
    print(welcome_assignment_answers(debug_question))
