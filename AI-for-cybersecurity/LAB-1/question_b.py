data = {
    "Monday":22,
    "Tuesday":34,
    "Wednesday":20,
    "Thursday":31,
    "Friday":29,
    "Saturday":25,
    "Sunday":27
}

print("Find and print the average (mean) temperature for the week..\n")
average = sum(data.values())/len(data)
print("Average:",average,"C")

print("Identify and print the maximum and minimum temperatures and their respective days.\n")
max_pair = max(data.items(), key=lambda item: item[1])
min_pair = min(data.items(), key=lambda item: item[1])
print("Maximum Temperature:",max_pair)
print("Minimum Temperature:",min_pair)

print("Display the temperatures greater than a specific value.\n")
temperature = float(input("Enter the value to check above: "))
for day, temp in data.items():
    if temp >= temperature:
        print(f"{day}: {temp}°C")

print("Convert all temperatures to Fahrenheit.\n")
for day,temp in data.items():
    data[day] = (temp*9/5)+32
print(data)

print("Print the days had temperatures above the average\n")
for day,temp in data.items():
    if temp>(average*9/5)+32:
        print(f"{day}:{temp}")
