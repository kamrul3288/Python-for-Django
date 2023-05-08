
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}


aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


# Emoji Converter Example
message = input("> ")
words = message.split(" ")
emoji = {
    ":D" : "🙂",
    ":)" : "😄",
    "(:" : "😞"
}
output = ""
for word in words:
    output += emoji.get(word, word) + " "
print(output)