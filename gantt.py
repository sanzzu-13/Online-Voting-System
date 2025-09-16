import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Define tasks and their durations
tasks = [
    ("Requirements Gathering and Planning", "2025-01-01", "2025-01-14"),
    ("System Design (UI/UX and Database Schema)", "2025-01-15", "2025-01-28"),
    ("User Authentication Module", "2025-01-29", "2025-02-11"),
    ("Election Management Module", "2025-02-12", "2025-02-25"),
    ("Voting Mechanism Implementation", "2025-02-26", "2025-03-10"),
    ("User Dashboard Development", "2025-03-11", "2025-03-24"),
    ("System Testing and Debugging", "2025-03-25", "2025-04-07"),
    ("Host on Localhost and Ensure Functionality", "2025-04-08", "2025-04-14"),
    ("Finalize Documentation and Training", "2025-04-15", "2025-04-28")
]

# Convert dates to datetime objects for plotting
task_names = [task[0] for task in tasks]
start_dates = [datetime.strptime(task[1], "%Y-%m-%d") for task in tasks]
end_dates = [datetime.strptime(task[2], "%Y-%m-%d") for task in tasks]
durations = [(end - start).days for start, end in zip(start_dates, end_dates)]

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot each task as a bar
for i, (task, start, duration) in enumerate(zip(task_names, start_dates, durations)):
    ax.barh(i, duration, left=start, color="skyblue", edgecolor="black")

# Format the chart
ax.set_yticks(range(len(task_names)))
ax.set_yticklabels(task_names)
ax.invert_yaxis()  # Invert y-axis to show tasks from top to bottom
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
plt.xticks(rotation=45)
ax.set_title("Gantt Chart for Online Voting System Development", fontsize=14, weight="bold")
ax.set_xlabel("Timeline", fontsize=12)
ax.set_ylabel("Tasks", fontsize=12)
plt.tight_layout()

# Show the plot
plt.show()
