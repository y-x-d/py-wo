def run_timing():
    running = True
    times = []
    total_time = 0
    while running:
        time = input("Enter 10 km run time: ")

        if not time:
            running = False
        elif not time.isnumeric():
            pass
        else:
            times.append(float(time))
    
    for time in times:
        total_time += time
    avg_time = total_time/len(times)
        
    print(f"Average of {avg_time}, over {len(times)} runs.")

run_timing()