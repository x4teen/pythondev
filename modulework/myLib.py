def center_text(width, *args):
    text = ""
    for arg in args:
        text += str(arg) + " "

    margin = " " * (width - len(text) // 2)
    print(margin, text)
    return len(margin)

