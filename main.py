import string

with open("packets.txt", "r") as file:
    rucksacks: list = file.read().split('\n')

lower_to_upper = string.ascii_lowercase+string.ascii_uppercase

merged_rucksacks = []
for i in range(0, len(rucksacks), 3):
    merged_item = [rucksacks[i], rucksacks[i+1], rucksacks[i+2]]
    merged_rucksacks.append(merged_item)

priority_sum = 0

for rucksack in merged_rucksacks:
    divider = int(len(rucksack)/2)
    part_one = set(rucksack[0])
    part_two = set(rucksack[1])
    part_three = set(rucksack[2])
    the_one = str(next(iter(part_one.intersection(part_two, part_three))))
    the_index = lower_to_upper.find(the_one)+1
    priority_sum += the_index

print(priority_sum)
