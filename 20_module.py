from utils import emoji_converter as converter

message = input("> ")
result = converter.emojiConverter(message)
print(result)