import webbrowser

browser = webbrowser.get()
# print(firefox)

target_url  = "https://www.facebook.com"

# webbrowser.open(target_url, new=1)
browser.open_new(target_url)

start = 200
limit = 225

print("{0:>10}".format("Number:"), end="")
for num01 in range(start, limit+1):
    print("{0:8,}".format(num01), end="")
print()
print('-' * ((limit-start+1)*8+10))


for num01 in range(start, limit+1):
    print("{0:8,}| ".format(num01), end="")
    for num02 in range(start, limit+1):
        print("{0:8,}".format(num01*num02), end="")
    print()