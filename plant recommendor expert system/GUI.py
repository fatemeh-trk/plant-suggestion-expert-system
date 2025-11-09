# app.py
import customtkinter as ctk
from experta import *
from expert_system import plantExpert, plantRec


class PlantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Apartment Plant Recommender")
        self.root.geometry("450x550")

        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("green")

        ctk.CTkLabel(root, text="🌿 Apartment Plant Recommender", font=("Arial", 20, "bold")).pack(pady=15)

        # Create dropdowns for each factor
        self.light = self._add_option("Light Level", ["low", "medium", "high"])
        self.humidity = self._add_option("Humidity Level", ["low", "medium", "high"])
        self.care = self._add_option("Care Difficulty", ["easy", "moderate", "difficult"])
        self.kid = self._add_option("Have Kids?", ["yes", "no"])
        self.water = self._add_option("Water Needs", ["low", "medium", "high"])
        self.space = self._add_option("Available Space", ["small", "medium", "large"])

        ctk.CTkButton(root, text="Get Recommendation", command=self.get_recommendation).pack(pady=20)


        self.result_label = ctk.CTkLabel(root, text="", font=("Arial", 14), wraplength=350)
        self.result_label.pack(pady=10)

    def _add_option(self, label, values):
        ctk.CTkLabel(self.root, text=label + ":").pack(pady=(10, 2))
        menu = ctk.CTkOptionMenu(self.root, values=values)
        menu.pack()
        return menu

    def get_recommendation(self):
        expert = plantExpert()
        expert.reset()

        expert.declare(plantRec(
            light=self.light.get(),
            humidity=self.humidity.get(),
            care=self.care.get(),
            kid_friendly=self.kid.get(),
            water=self.water.get(),
            space=self.space.get()
        ))

        expert.run()

        plant_name, info_text = None, None
        for fact in expert.facts.values():
            if isinstance(fact, Fact) and 'plant' in fact:
                plant_name = fact['plant']
                info_text = fact.get('info', '')
                break

        if plant_name:
            self.result_label.configure(
                text=f"✅ Recommended Plant:\n{plant_name}\n\n{info_text}"
            )

        else:
            self.result_label.configure(
                text="⚠️ No suitable plant found.\nTry different preferences."
            )

        info_window = ctk.CTkToplevel(self.root)
        info_window.title(f"About {plant_name}")
        info_window.geometry("400x250")

        ctk.CTkLabel(info_window, text=f"🌱 {plant_name}",
                 font=("Arial", 18, "bold")).pack(pady=10)
        ctk.CTkLabel(info_window, text=info_text,
                 font=("Arial", 14), wraplength=350, justify="center").pack(pady=10)
        ctk.CTkButton(info_window, text="Close", command=info_window.destroy).pack(pady=15)

if __name__ == "__main__":
    root = ctk.CTk()
    app = PlantApp(root)
    root.mainloop()



