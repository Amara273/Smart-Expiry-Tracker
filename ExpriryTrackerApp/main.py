import customtkinter as ctk
from loginsystem import App
from ExpiryTracker import SmartGroceryTrackerUI

def switch_to_expiry_tracker(self):
    for w in self.winfo_children():
        w.destroy()
    
    tracker = SmartGroceryTrackerUI(self)
    # tracker.(fill="both", expand=True)

App.switch_to_expiry_tracker = switch_to_expiry_tracker 
if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")
    app = App()
    app.mainloop()
    