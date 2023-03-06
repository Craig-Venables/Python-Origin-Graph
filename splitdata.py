def split_endurance_sweep(working_folder,filename):
    file_path = working_folder + 'data\\endurance\\Endurance 1.8v.txt'
    print(file_path)
    data = []

    # Extract voltage from filename using regular expression
    match = re.search(r"voltage_(\d+)V_", filename)
    if match:
        voltage = int(match.group(1))
        print("Voltage:", voltage)
    else:
        print("Error: could not extract voltage from filename")

    with open(file_path, "r") as file:
        next(file)  # Skip the header line
        for line in file:
            # Split the line into two groups of three values and convert them to float
            values = line.strip().split()
            values = [float(x) for x in values[1:]]  # Ignore the first value of each group
            data.append(values)

    # Separate the columns into individual arrays and remove the titles
    iteration = [row[0] for row in data][1:]
    time_set = [row[1] for row in data][1:]
    current_set = [row[2] for row in data][1:]
    time_reset = [row[3] for row in data][1:]
    current_reset = [row[4] for row in data][1:]

    # Print the results
    print("Iteration:", iteration)
    print("Time (Set):", time_set)
    print("Current (Set):", current_set)
    print("Time (Reset):", time_reset)
    print("Current (Reset):", current_reset)

print (working_folder)
split_endurance_sweep( working_folder,"Endurance 1.8v")
