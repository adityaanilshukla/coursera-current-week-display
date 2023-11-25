import requests
from bs4 import BeautifulSoup
import tkinter as tk

def get_current_week():
    url = "https://github.com/world-class/REPL"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the ul element with the specified pattern
    ul_element = soup.find('ul', {'dir': 'auto'})
    
    if ul_element:
        # Find the li element within the ul
        li_element = ul_element.find('li')
        
        if li_element:
            # Extract the week number from the li element and remove the dot
            week_number = li_element.text.split()[1].replace('.', '')
            return week_number

    return None

def show_week_window():
    current_week = get_current_week()

    #number of seconds after which to close the window
    destroy_time = 10000

    # Create a simple Tkinter window
    window = tk.Tk()
    window.title("Coursera UOL Comp Science Current Week")

    # Set window attributes for transparency
    window.attributes('-alpha', 0.8)  # Set transparency level (0.0 to 1.0)

    # Display the current week in the window with white text on a black background
    label_text = f"UOL CS Week: {current_week}" if current_week else "Unable to determine the current week."
    label = tk.Label(window, text=label_text, font=('Helvetica', 20, 'bold'), fg='white', bg='black')
    label.pack(padx=20, pady=20)

    # Set window color
    window['bg']='black'

    window.after(destroy_time, lambda: window.destroy())  # Destroy the widget after a set amount of seconds

    # Run the Tkinter event loop
    window.mainloop()

if __name__ == "__main__":
    show_week_window()
