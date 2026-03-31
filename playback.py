user_text = input("Type something: ")

#First we .split() the text into pieces,
# then we .join() them with dots
print('...'.join(user_text.split()))