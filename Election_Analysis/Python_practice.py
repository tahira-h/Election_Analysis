counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

# Let's practice creating a memebership operation by determining if "El Paso" is in the counties list
counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else: 
    print("El Paso is not the list of counties")

#Use "and" operator to determine if two counties, Arapahoe and El Paso, are in the list of counties"

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

# Let's check if either "Arapahoe" or "El Paso" is in the counties list. By replacing the logical operator "and" with "or" and run the file.

if "Araphahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")


# Create and implement a for loop by iterating through the lsit of counties.

for county in counties:
    print(county)

# For Loop/Dictionaries (2) parts
# Part 1
# Use a for loop to iterate over a dictionary and get all the keys, all the values, or all the keys and values.
# Use the counties dictionary that was created earlier.

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# Part 2
#Now get only the keys from a dictionary using a for loop, the loop can be written like we are interating over a list or tuple. 
for county in counties_dict:
    print(county)
#EXECUTE!

# Use the keys() method to iterate over a dictionary to get the keys. 
# To the previous code, add the keys() method to the end of the counties_dict.
for county in counties_dict.keys():
    print(county)

# Get the values of a Dictionary
# Iterate over the dictionary using the values() method, just like we used the keys() method
for voters in counties_dict.values():
    print(voters)

# Use the format dictionary_name[key] to get the value for the key.
# When using the format dictionary_name[key], include the key county int he for loop in the print statement.
# This will return the value of the key in the output.
# For the counties list, modify the for loop and use the key, county to reference the value. 
for county in counties_dict:
    print(counties_dict[county])

# Another method we can use to get the values of a key is to use the get() method on the dictionary in the for loop.
for county in counties_dict:
    print(counties_dict.get(county))

# If we want to print the key-value pair of the dictionary, we use the items() method in the for loop. 
# for key, value in dictionary_name.items():
#    print(key, value)

# When we use the items() method, we get the key and the value for each dictionary by referencing them as "key" and "value" as in the code above, or we can reference them by name, like "county" and "voters".
for county, voters in counties_dict.items():
    print(county, voters)
#EXECUTE!

# Iterate through a list of Dictionaries
# To print each dictionary in voting_data, use the standard format for iterating over the list of dictionaries with a for loop:
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
    {"county":"Denver", "registered_voters": 463353},
    {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

# To retrieve only the values from each dictionary in the list of dictionaries, we need to use a nested for loop.
# Use the for loop: for county_dict in voting_data: to retrieve each dictionary
# In the 2nd for loop, use the values() method on the variable county_dict to reference the data in the second for loop in order to get each value.
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
# EXECUTE!

# To only print the county name from each dictionary, we can use county_dict['county'] in the print statement for the for loop.
for county_dict in voting_data:
    print(county_dict['county'])
# EXECUTE!


# F-Strings: Formatted String Literals
# Edit the code we wrote to calculate the percentage of votes using f-string literals.
# Original code below:
# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")

# Here's how to edit the code to use f-strings below:
# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# print(f"I received {my_votes / total_votes * 100}% of the total votes.")

# Using F-Strings with Dictionaries
# Here's the counties dictionary and the solution if we use concatenation.

#counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
#for county, voters in counties_dict.items():
#    print(county + " county has " + str(voters) + " registered voters.")

# Rewrite the print statement to be more intuitive and clear.
#for county, voters in counties_dict.items():
#    print(f"{county} county has {voters} registered voters.")

# Multiline F-Strings
# Do you need to tell a candidate how many votes they won, the total number of votes, and the percentage of votes they received?
# You can use the code you wrote to calculate the percentage of votes and create a message to be printed to a screen. 
# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#    f"You received {candidate_votes} number of votes. "
#    f"The total number of votes in the election was {total_votes}. "
#    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

#print(message_to_candidate)
#EXECUTE!

# Format Floating-Point Decimals
# The general format for a number to format it in an f-string is as follows:
#f'{value:{width}.{precision}}'

# When formatting a number, we can also add a thousands separator with a comma, using the following format. The comma is placed after the {width}.
#f'{value:{width},.{precision}}'

# Let's add a thousands separator to the output for the candidates votes and total votes and then format the percentage of votes to two decimal places. 
#message_to_candidate = (
#    f"You received {candidate_votes:,} number of votes."
#    f"The total number of votes in the election was {total_votes:,}. "
#    f"You received {candidate_votes / total_votes * 100: .2f}% of the total votes.")






