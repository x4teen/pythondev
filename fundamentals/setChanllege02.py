sample_text = input("Enter a quote : ")
vowels = {"a", "e", "i", "o", "u", " ", ",", ".", "!", "?"}
text_characters = set(sample_text).difference(vowels)

print(sorted(text_characters))
