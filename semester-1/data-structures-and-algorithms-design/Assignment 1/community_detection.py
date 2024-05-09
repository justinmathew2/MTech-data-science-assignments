import os


def read_input():
    # Read the input data from the file and create a list
    if os.path.exists("inputPS06.txt"):
        with open("inputPS06.txt", "r", encoding='utf-8-sig') as f:
            data = [line.strip() for line in f]

            if len(data) == 0:
                print("File is empty, please provide a valid input file")
            else:
                return data
    else:
        print("file doesn't exist, please provide the file")


def process_data(data):
    # Create a list of lists to store the groups and their participants
    groups = []

    # Iterate through the input data
    for entry in data:
        # Split the entry into the two participants
        if '/' in entry:
            p1, p2 = entry.split("/")
        else:
            print("input file format is invalid")
            break

        # Check if the participants are already in the list of lists
        found = False
        for group in groups:
            if p1 in group or p2 in group:
                # Add the other participant to the group
                group.add(p1)
                group.add(p2)
                found = True
                # print(group)
                break

        if not found:
            # Check if the participants are in another group
            for group in groups:
                if p1 in group or p2 in group:
                    # Merge the two groups
                    if len(group) < len([p1, p2]):
                        group.update([p1, p2])
                    else:
                        [p1, p2].update(group)
                        groups.remove(group)
                        groups.append([p1, p2])
                    found = True
                    break

            if not found:
                # Create a new list for the participants
                groups.append(set([p1, p2]))

    return groups


def create_output(groups):
    # Create the output string for each group
    output = ""
    for i, group in enumerate(groups):
        participants = ", ".join(group)
        output += f"Group {i + 1}: There are {len(group)} participants in the group and they are {participants}\n"

    # print(output)
    return output


def write_output(output):
    # Write the output string to the output file
    with open("outputPS06.txt", "w") as f:
        f.write(output)


# Main function
def main():
    data = read_input()
    groups = process_data(data)
    output = create_output(groups)
    write_output(output)
    print("outfile is created with name outputPS06.txt")


# Run the main function
main()
