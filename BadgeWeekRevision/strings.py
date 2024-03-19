# reverse string
def reverse_string(s):
    return s[::-1]

print(reverse_string("Hrishikesh"))

# palendrome
def palendrome(s):
    if s == s[::-1]:
        print("Palendrome ")
    else:
        print("Not Palendrome")

palendrome("malayalam")
palendrome("Hrishikesh")

# Count vowels
def count_vowels(s):
    vow = "aeiouAEIOU"
    vow_count = sum(1 for i in s if i in vow)
    cons_count = len(s) - vow_count
    print(vow_count)
    print(cons_count)
    return

count_vowels("Hrishikesh")


# remove duplicates
def remove_duplicates(s):
    res = ""
    for i in s:
        if i not in res:
            res+=i

    print(res)
    return 

remove_duplicates('Hrishikesh')

# count words
def count_words(s):
    words= s.split()
    return len(words)

print(count_words("Hrishikesh is Good"))


