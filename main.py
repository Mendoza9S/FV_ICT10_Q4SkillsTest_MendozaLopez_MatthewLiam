from pyscript import document
import numpy as np
import matplotlib.pyplot as plt


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

absences = np.array([0, 0, 0, 0, 0])


def submit_attendance():
    day = document.getElementById("day").value
    absence = document.getElementById("absences").value
    message = document.getElementById("message")

    if absence == "":
        message.innerHTML = "Please enter absences."
        return

    absence = int(absence)

    index = days.index(day)
    absences[index] = absence

    message.innerHTML = f"{day} recorded!"

    document.getElementById("absences").value = ""


def display_graph():
    plt.figure()

    plt.plot(days, absences, marker='o')

    plt.title("Weekly Attendance (Absences)")
    plt.xlabel("Day")
    plt.ylabel("Absences")

    plt.show()
