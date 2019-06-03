import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib.animation as animation
import datetime as dt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Configure tkinter window
root = tk.Tk()
root.configure(bg = "black")
root.geometry("800x480")

plt.style.use('dark_background')

#Patient information
patient_name="Omar Muttawa"
dob_str='14031998'
doctor_name="XXX YYY"

# Apply appropriate formatting to axes
def format_axis(id, ax):
    if id == 'e':
        ax.set_ylabel('V', fontsize=8)
        ax.set_title("ECG",fontsize=9)
    elif id == 'p':
        ax.set_ylabel('PPG unit', fontsize=8)
        ax.set_title("PPG",fontsize=9)
    else:
        ax.set_ylabel('rpm', fontsize=8)
        ax.set_title("Respiration",fontsize=9)
    ax.set_xlabel("Time", fontsize=8)
    for tick in ax.get_xticklabels():
        tick.set_fontsize(6)
    for tick in ax.get_yticklabels():
        tick.set_fontsize(6)

# Update graph
def plotter(id, ax, xar, yar):
    ax.cla()
    if id == 'e':
        format_axis('e', ax)
        ax.plot(xar, yar, color="green")
        graph_ecg.draw()
    elif id == 'p':
        format_axis('p', ax)
        ax.plot(xar, yar, color="yellow")
        graph_ppg.draw()
    else: 
        format_axis('r', ax)
        ax.plot(xar, yar, color="blue")
        graph_resp.draw()

# Set critical flag when report issue button is pressed - send this info to DB
def report():
    critical = True
    critical_time = dt.datetime.utcnow()

#Heart Rate Digital Initilisation
hr_info1 = tk.Label(root, text = "Heart Rate:", fg="green", bg="black", font=("Arial",14))
hr_info2 = tk.Label(root, text = "--", fg="green", bg="black", font=("Arial", 40))
hr_info3 = tk.Label(root, text = "bpm", fg="green", bg="black", font=("Arial", 14))
hr_info1.grid(row=1, column=2)
hr_info2.grid(row=2, column=2)
hr_info3.grid(row=3, column=2)
#SPO2 Digital Initilisaton
spo2_info1 = tk.Label(root, text = "SpO2:", fg="yellow", bg="black", font=("Arial",14))
spo2_info2 = tk.Label(root, text = "--", fg="yellow", bg="black", font=("Arial", 40))
spo2_info3 = tk.Label(root, text = "%", fg="yellow", bg="black", font=("Arial", 14))
spo2_info1.grid(row=4, column=2)
spo2_info2.grid(row=5, column=2)
spo2_info3.grid(row=6, column=2)
#Temperature Digital Inilisation
temp_info1 = tk.Label(root, text = "Temperature:", fg="red", bg="black", font=("Arial",14))
temp_info2 = tk.Label(root, text = "--", fg="red", bg="black", font=("Arial", 40))
temp_info3 = tk.Label(root, text = "˚C", fg="red", bg="black", font=("Arial", 14))
temp_info1.grid(row=7, column=2)
temp_info2.grid(row=8, column=2)
temp_info3.grid(row=9, column=2)

# Respiration Rate
resp_info1 = tk.Label(root, text = "Respiration Rate:", fg="blue", bg="black", font=("Arial",14))
resp_info2 = tk.Label(root, text = "--", fg="blue", bg="black", font=("Arial", 40))
resp_info3 = tk.Label(root, text = "˚C", fg="blue", bg="black", font=("Arial", 14))
resp_info1.grid(row=10, column=2)
resp_info2.grid(row=11, column=2)
resp_info3.grid(row=12, column=2)

def display_digital(connection_status,patient_name,dob_str,doctor_name,hr,spo2,temp,resp):
    # Connection status
    #connected = True
    if connection_status:
       connection_status = tk.Label(root, text = "Connected", fg="green", bg="black")
       connection_status.grid(row=0, column=2)
    else:
       connection_status = tk.Label(root, text = "Disconnected", fg="red", bg="black")
       connection_status.grid(row=0, column=2)

    # Patient information - input from DB
    #patient_name = "John Smith"
    #dob_str = '010100'
    dob_obj = dt.datetime.strptime(dob_str, '%d%m%y')
    patient_info = tk.Label(root, text = "Name: "+patient_name+"  DOB: "+dt.datetime.strftime(dob_obj, '%d/%m/%y'), fg="white", bg="black")
    patient_info.grid(row=0, column=0, sticky='W')
    # Doctor information - input from DB
    #doctor_name = "Dr. XXX YYY"
    doctor_info = tk.Label(root, text = "Doctor: "+doctor_name, fg="white", bg="black")
    doctor_info.grid(row=0, column=1, sticky='W')
    # Heart Rate
    hr_info2 = tk.Label(root, text = str(hr), fg="green", bg="black", font=("Arial", 40))
    # SpO2
    spo2_info2 = tk.Label(root, text = str(spo2), fg="yellow", bg="black", font=("Arial", 40))
    # Temperature
    temp_info2 = tk.Label(root, text = str(temp), fg="red", bg="black", font=("Arial", 40))
    # Respiration Rate
    resp_info2 = tk.Label(root, text = str(resp), fg="blue", bg="black", font=("Arial", 40))
    
# Graphs
xar = [] # Time array
y_ecg = [] # ECG data array
y_ppg = [] # PPG data array
y_resp = [] # Respiration data array
x=1

# ECG Graph pane
fig_ecg = Figure(figsize=(6.7,1.3), constrained_layout=True)
ax_ecg = fig_ecg.add_subplot(111)
format_axis('e', ax_ecg)
graph_ecg = FigureCanvasTkAgg(fig_ecg, master=root)
graph_ecg.get_tk_widget().grid(row=1, column=0, columnspan=2, rowspan=4)

# PPG Graph pane
fig_ppg = Figure(figsize=(6.7,1.3), constrained_layout=True)
ax_ppg = fig_ppg.add_subplot(111)
format_axis('p', ax_ppg)
graph_ppg = FigureCanvasTkAgg(fig_ppg, master=root)
graph_ppg.get_tk_widget().grid(row=5, column=0, columnspan=2, rowspan=4)

# Respiration Graph pane
fig_resp = Figure(figsize=(6.7,1.3), constrained_layout=True)
ax_resp = fig_resp.add_subplot(111)
format_axis('r', ax_resp)
graph_resp = FigureCanvasTkAgg(fig_resp, master=root)
graph_resp.get_tk_widget().grid(row=9, column=0, columnspan=2, rowspan=4)

# Report issue button
report_button = tk.Button(root, text="REPORT ISSUE", command=report, width=70, height=2, fg="white", highlightbackground="black", bg="gray", activebackground="red")
report_button.grid(row = 13, column=0, columnspan = 2, sticky='E')

# Update graph in real time
def animate(i, xar, y_ecg, y_ppg, y_resp,patient_name,dob_str,doctor_name):
    global x
    global ecg
    global ppg
    global resp

    # Read data into arrays
    xar.append(dt.datetime.utcnow())
    y_ecg.append(ecg) 
    y_ppg.append(ppg)
    y_resp.append(resp)

    # Limit arrays to store only the most recent 20 readings
    xar = xar[-20:]
    y_ecg = y_ecg[-20:]
    y_ppg = y_ppg[-20:]
    y_resp = y_resp[-20:]

    # remove - just for RT testing
    x += 1
    display_digital(connection_status,patient_name,dob_str,doctor_name,hr,spo2,temp,resp)
    # Produce ECG plot
    plotter('e', ax_ecg, xar, y_ecg)

    # Produce PPG plot
    plotter('p', ax_ppg, xar, y_ppg)

    # Produce respiration plot
    plotter('r', ax_resp, xar, y_resp)

ani = animation.FuncAnimation(fig_ecg, animate, fargs = (xar, y_ecg, y_ppg, y_resp,patient_name,dob_str,doctor_name), interval=1000) # animate graph every 1000 ms

root.mainloop() # tkinter GUI window
