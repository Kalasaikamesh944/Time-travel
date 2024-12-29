import math
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import table

class TimeTravelResearch:
    def __init__(self):
        print("Debug: TimeTravelResearch initialized.")

    def calculate_relativistic_speed(self, mass):
        print(f"Debug: Calculating relativistic speed for mass {mass} kg.")
        c = 3e8
        if mass <= 0:
            raise ValueError("Mass must be a positive value.")
        speed = c * math.sqrt(1 - (mass / (mass + c)) ** 2)
        print(f"Debug: Relativistic speed for mass {mass} kg is {speed:.2e} m/s.")
        return speed

    def calculate_required_speed(self, mass, target_fraction):
        print(f"Debug: Calculating required speed for mass {mass} kg to reach {target_fraction * 100:.1f}% of the speed of light.")
        c = 3e8
        target_speed = target_fraction * c
        speed = c * math.sqrt(1 - (mass / (mass + c)) ** 2)
        if speed >= target_speed:
            print(f"Debug: Mass {mass} kg can reach {speed:.2e} m/s, which matches {target_fraction * 100:.1f}% of the speed of light.")
            return speed
        else:
            print(f"Debug: Mass {mass} kg cannot reach the target speed of {target_speed:.2e} m/s.")
            return speed

    def calculate_energy(self, mass):
        print(f"Debug: Calculating energy for mass {mass} kg.")
        c = 3e8
        energy = mass * c**2
        print(f"Debug: Energy for mass {mass} kg is {energy:.2e} J.")
        return energy

    def calculate_for_all_masses(self, target_fraction):
        print("Debug: Calculating for all masses from 1kg to 100kg.")
        results = []
        for mass in range(1, 101):
            speed = self.calculate_required_speed(mass, target_fraction)
            energy = self.calculate_energy(mass)
            speed_kmh = speed * 3.6  # Convert m/s to km/h
            results.append((mass, speed_kmh, energy))
            print(f"Mass: {mass} kg, Speed: {speed_kmh:.2e} km/h, Energy: {energy:.2e} J")
        return results

    def display_results_as_table(self, results):
        print("Debug: Displaying results as a table.")
        df = pd.DataFrame(results, columns=["Mass (kg)", "Speed (km/h)", "Energy (J)"])
        print(df.to_string(index=False))
        return df

    def save_table_as_image(self, df, filename="table_image.png"):
        print("Debug: Saving table as an image.")
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.axis('tight')
        ax.axis('off')
        table(ax, df, loc='center', cellLoc='center')
        plt.savefig(filename, bbox_inches='tight')
        print(f"Table saved as {filename}.")


def main():
    try:
        print("Debug: Starting main function.")
        time_travel = TimeTravelResearch()

        target_fraction = 0.999  # Targeting 99.9% of the speed of light

        print("Debug: Calculating for all masses from 1kg to 100kg.")
        results = time_travel.calculate_for_all_masses(target_fraction)

        print("Debug: Displaying results as a table.")
        df = time_travel.display_results_as_table(results)

        print("Debug: Saving table as an image.")
        time_travel.save_table_as_image(df)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
