import tkinter as tk
import random

class DiceRollingSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Visual Dice Roller")
        self.root.geometry("400x450")
        self.root.configure(bg="#121212")  # Deep Black background for high contrast

        # Dice faces using Unicode characters for high-quality scaling
        self.dice_faces = {
            1: "⚀",
            2: "⚁",
            3: "⚂",
            4: "⚃",
            5: "⚄",
            6: "⚅"
        }

        # Title Label
        self.title_label = tk.Label(
            root, 
            text="Single Die Roller", 
            font=("Helvetica", 24, "bold"), 
            bg="#121212", 
            fg="#00FFD1"  # Neon Cyan title
        )
        self.title_label.pack(pady=30)

        # Frame to hold the dice
        self.dice_frame = tk.Frame(root, bg="#121212")
        self.dice_frame.pack(pady=10)

        # Die 1 Label
        self.die1_label = tk.Label(
            self.dice_frame, 
            text="⚀", 
            font=("Times New Roman", 140), 
            bg="#121212", 
            fg="#FFFFFF"  # Pure White die for maximum contrast
        )
        self.die1_label.pack()

        # Result Label (Total)
        self.result_label = tk.Label(
            root, 
            text="Rolled: 1", 
            font=("Helvetica", 18), 
            bg="#121212", 
            fg="#FFD700"  # Gold for the result text
        )
        self.result_label.pack(pady=20)

        # Roll Button
        self.roll_button = tk.Button(
            root, 
            text="ROLL", 
            font=("Helvetica", 14, "bold"), 
            bg="#FF0055",  # Vibrant Hot Pink button
            fg="white", 
            activebackground="#CC0044",
            activeforeground="white",
            command=self.roll_dice,
            padx=40,
            pady=10,
            relief="flat"
        )
        self.roll_button.pack(pady=20)

    def roll_dice(self):
        """Generates random numbers and updates the UI."""
        val1 = random.randint(1, 6)
        
        # Update dice graphics
        self.die1_label.config(text=self.dice_faces[val1])
        
        # Update total score
        self.result_label.config(text=f"Rolled: {val1}")

        # Simple animation effect (flash color)
        self.flash_effect()

    def flash_effect(self):
        """Briefly changes text color to simulate action."""
        original_color = "#FFFFFF"
        flash_color = "#00FFD1" # Flash Cyan
        
        self.die1_label.config(fg=flash_color)
        
        # Revert color after 200ms
        self.root.after(200, lambda: self.die1_label.config(fg=original_color))

if __name__ == "__main__":
    root = tk.Tk()
    app = DiceRollingSimulator(root)
    root.mainloop()