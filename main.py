# attendance_tracker/main.py
import matplotlib.pyplot as plt
import numpy as np
from pyscript import document, display

# 1. Create our list of days and our data storage
# We use np.zeros(5) to start with 5 zeros: [0, 0, 0, 0, 0]
days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
absence_data = np.zeros(5, dtype=int)

def handle_submit(event):
    """This function runs when the Submit button is clicked"""
    
    # Get the elements from the HTML page
    day_dropdown = document.getElementById("day")
    absence_input = document.getElementById("absences")
    status_message = document.getElementById("message")

    # Check if the user actually typed a number
    if absence_input.value == "":
        status_message.innerText = "Error: Enter a number first!"
        return

    # Find which day was picked (Monday is 0, Tuesday is 1, etc.)
    selected_day = day_dropdown.value
    day_index = days_list.index(selected_day)

    # Save the number of absences into our NumPy array
    absence_data[day_index] = int(absence_input.value)

    # Show a success message to the user
    status_message.innerText = f"Success! {selected_day} updated."
    
    # Clear the input box for the next entry
    absence_input.value = ""

    # Refresh the graph so we can see the changes
    generate_graph()

def generate_graph():
    """This function creates the line graph using Matplotlib"""
    
    # Clear the old graph so they don't stack on top of each other
    plt.clf()

    # Create the plot (X-axis = days, Y-axis = absences)
    # marker='o' adds dots, linestyle='-' adds the line
    plt.plot(days_list, absence_data, marker='o', linestyle='-', color='blue')

    # Add labels and titles so it's easy to read
    plt.title("Weekly Attendance (Absences)")
    plt.xlabel("Day of the Week")
    plt.ylabel("Number of Absences")
    
    # Add a grid to make the points easier to see
    plt.grid(True)

    # Show the graph inside the "graph-output" div in the HTML
    display(plt.gcf(), target="graph-output", append=False)

# This makes the graph show up as soon as the page loads
generate_graph()