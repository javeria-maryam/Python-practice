# 1. Make a dictionary of 5 countries with thier capitals. Ask user to enter a country and print its capital.

countries = { "pakistan" : "Islamabad",
             "afghanistan" : "Kabul",
             "canada" : "Ottowa",
             "india" : "New Delhi",
             "america" : "Washington D.C."
}

country = input("Enter a country name to know its capital: ").lower()

if country in countries:
    print("The capital of",country.capitalize(),"is",countries[country])

else:
    print("Sorry, the country is not present in the list")


# 2. Write a program that counts how many times each letter appears in a word (using dictionary).

word = input("Enter any word: ")

letter_count = {}

for letter in word:
    if letter in letter_count:
        letter_count[letter]+=1

    else:
        letter_count[letter]= 1

print(letter_count)




# 3. Take a list with duplicates, convert it into a set to remove duplicates.

thislist = [2,9,0,9,0,6,7,7]

thislist = set((thislist))

print(thislist)