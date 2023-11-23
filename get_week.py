
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
            # Extract the week number from the li element
            week_number = li_element.text.split()[1]
            return week_number

    return None

def show_week_window():
    current_week = get_current_week()

    # Create a simple Tkinter window
    window = tk.Tk()
    window.title("Current Week")

    # Display the current week in the window
    label_text = f"Current Week: {current_week}" if current_week else "Unable to determine the current week."
    label = tk.Label(window, text=label_text)
    label.pack(padx=20, pady=20)

    # Run the Tkinter event loop
    window.mainloop()

if __name__ == "__main__":
    show_week_window()
