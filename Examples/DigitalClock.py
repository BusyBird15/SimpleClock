# Digital clock v1.0, made with SimpleClock.

# Import SimpleClock, no need for time!
import SimpleClock as sc

# We will use this format through the entire script. This is not necessary, but makes the code easier to type.
format= "HH:MM:SS"


# We always want this clock to print.
while True:
    # Fetch the time in HH:MM:SS format for Eastern timezone, wich is UTC-4:
    clock_time = sc.formatted_time(format, -4)
    # Print and rewrite a line of output to the console.
    print("\r" + clock_time, end=0)
    # Wait until the clock time changes from clock_time, which had a predefined format of "HH:MM:SS".
    sc.wait_for_clock_change(clock_time, format)
    # After the code resumes, the clock will be printed again.

