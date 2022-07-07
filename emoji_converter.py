message = input(">")
words = message.split(' ')  # split the string on white space
emojis = {
    ":)": "😊",
    ":(": "😢"
}
output = ""  # Empty string for the replacement
for word in words:
    output += emojis.get(word, word) + " "  # create output add the word if the value matches the key, if no item use
    # that word as default value
print(output)
