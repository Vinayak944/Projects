def emoji_converter(message):
    emoji = {":)": 'smile',":(": 'sad'}
    output = ''
    for word in message.split(" "):
        output += emoji.get(word , word) + " "
    return output
messages = input('>')
print(emoji_converter(messages))