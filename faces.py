user_text = input("Type in text with emoticon :) or :( - ")

user_text = user_text.replace(":)", "😊")
user_text = user_text.replace(":(", "😢")

print(user_text)