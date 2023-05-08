
def emojiConverter(message:str):
    words = message.split(" ")
    emoji = { ":D" : "🙂", ":)" : "😄", "(:" : "😞"}
    output = ""
    for word in words:
        output += emoji.get(word, word) + " "
    return output