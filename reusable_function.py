def emoji_converter(message):
    words = message.split(' ')  # split the string on white space
    emojis = {
        ":)": "😊",
        ":(": "😢"
    }
    output = ""  # Empty string for the replacement
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message: str = input(">")
print(emoji_converter(message))  # Call the function and pass message as the argument while printing in the same line
