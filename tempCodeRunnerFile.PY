def input_processes():
    processes = []
    n = int(input("Enter number of processes (up to 20): "))
    if n > 20:
        print("Limit is 20.")
        return input_processes()

    for i in range(n):
        print(f"\nProcess {i+1}")
        at = int(input("Enter Arrival Time: "))
        bt = int(input("Enter Burst Time: "))
        processes.append([i+1, at, bt])
    return processes

def schedule_fcfs(processes):
    processes.sort(key=lambda x: x[1])  # Sort by arrival time
    time = 0
    result = []
    total_wt = 0
    total_tat = 0

    for p in processes:
        pid, at, bt = p
        st = max(time, at)
        ct = st + bt
        tat = ct - at
        wt = tat - bt
        result.append([pid, at, bt, st, ct, tat, wt])
        time = ct
        total_wt += wt
        total_tat += tat

    avg_wt = total_wt / len(processes)
    avg_tat = total_tat / len(processes)
    return result, avg_wt, avg_tat

def display_gantt_chart(result):
    print("\nGantt Chart:")
    print(" ", end="")
    for r in result:
        print("-------", end="")
    print()
    print("|", end="")
    for r in result:
        print(f" P{r[0]}  |", end="")
    print()
    print(" ", end="")
    for r in result:
        print("-------", end="")
    print()
    print(result[0][3], end="")
    for r in result:
        print(f"\t{r[4]}", end="")
    print("\n")

def display_table(result):
    print("\nPID\tAT\tBT\tST\tCT\tTAT\tWT")
    for r in result:
        print(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}\t{r[4]}\t{r[5]}\t{r[6]}")

def show_analysis(result, avg_wt, avg_tat):
    wt_list = [r[6] for r in result]
    tat_list = [r[5] for r in result]

    wt_list.sort()
    tat_list.sort()
    mid = len(wt_list) // 2
    if len(wt_list) % 2 == 0:
        median_wt = (wt_list[mid-1] + wt_list[mid]) / 2
        median_tat = (tat_list[mid-1] + tat_list[mid]) / 2
    else:
        median_wt = wt_list[mid]
        median_tat = tat_list[mid]

    print("\n--- Statistics ---")
    print(f"Average Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")
    print(f"Minimum Waiting Time: {min(wt_list)}")
    print(f"Maximum Waiting Time: {max(wt_list)}")
    print(f"Median Waiting Time: {median_wt:.2f}")
    print(f"Minimum Turnaround Time: {min(tat_list)}")
    print(f"Maximum Turnaround Time: {max(tat_list)}")
    print(f"Median Turnaround Time: {median_tat:.2f}")

def save_report(result, avg_wt, avg_tat):
    with open("fcfs_full_report.txt", "w") as f:
        f.write("PID\tAT\tBT\tST\tCT\tTAT\tWT\n")
        for r in result:
            f.write(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}\t{r[4]}\t{r[5]}\t{r[6]}\n")
        f.write(f"\nAverage Waiting Time: {avg_wt:.2f}\n")
        f.write(f"Average Turnaround Time: {avg_tat:.2f}\n")
    print("Report saved to fcfs_full_report.txt")

def sort_results(result):
    print("\nSort By:")
    print("1. Process ID")
    print("2. Waiting Time")
    print("3. Turnaround Time")
    choice = input("Enter choice: ")
    if choice == "1":
        result.sort(key=lambda x: x[0])
    elif choice == "2":
        result.sort(key=lambda x: x[6])
    elif choice == "3":
        result.sort(key=lambda x: x[5])
    else:
        print("Invalid. Showing unsorted.")
    return result

def menu():
    global processes, result, avg_wt, avg_tat
    processes = []
    result = []
    avg_wt = 0
    avg_tat = 0

    while True:
        print("\n==== FCFS Scheduler Menu ====")
        print("1. Input Processes")
        print("2. Schedule FCFS")
        print("3. Display Gantt Chart")
        print("4. Display Process Table")
        print("5. Show Analysis")
        print("6. Sort Results")
        print("7. Save Report")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            processes = input_processes()
        elif choice == "2":
            if processes:
                result, avg_wt, avg_tat = schedule_fcfs(processes)
                print("Scheduling Done.")
            else:
                print("Please input processes first.")
        elif choice == "3":
            if result:
                display_gantt_chart(result)
            else:
                print("No scheduling data.")
        elif choice == "4":
            if result:
                display_table(result)
            else:
                print("No results to show.")
        elif choice == "5":
            if result:
                show_analysis(result, avg_wt, avg_tat)
            else:
                print("Please schedule first.")
        elif choice == "6":
            if result:
                result = sort_results(result)
                print("Sorted successfully.")
            else:
                print("No results yet.")
        elif choice == "7":
            if result:
                save_report(result, avg_wt, avg_tat)
            else:
                print("Nothing to save.")
        elif choice == "8":
            print("Exiting FCFS Scheduler.")
            break
        else:
            print("Invalid choice. Try again.")

# Start the program
menu()
