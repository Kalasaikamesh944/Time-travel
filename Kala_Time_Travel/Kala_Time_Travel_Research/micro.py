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

    def calculate_required_speed(self, mass):
        print(f"Debug: Calculating required speed for mass {mass} kg to match the speed of light.")
        c = 3e8
        speed = c * math.sqrt(1 - (mass / (mass + c)) ** 2)
        print(f"Debug: Mass {mass} kg achieves a speed of {speed:.2e} m/s.")
        return speed

    def calculate_energy(self, mass):
        print(f"Debug: Calculating energy for mass {mass} kg.")
        c = 3e8
        energy = mass * c**2
        print(f"Debug: Energy for mass {mass} kg is {energy:.2e} J.")
        return energy

    def calculate_micro_particles(self):
        print("Debug: Calculating for micro-particles (proton, neutron, electron, muon, neutrino).")
        particles = {
            "Proton": 1.6726219e-27,  # in kg
            "Neutron": 1.6749275e-27, # in kg
            "Electron": 9.10938356e-31, # in kg
            "Muon": 1.8835316e-28,    # in kg
            "Neutrino": 1.0e-36       # estimated upper limit in kg
        }
        results = []
        for particle, mass in particles.items():
            speed = self.calculate_required_speed(mass)
            energy = self.calculate_energy(mass)
            speed_kmh = speed * 3.6  # Convert m/s to km/h
            results.append((particle, mass, speed_kmh, energy))
            print(f"Particle: {particle}, Mass: {mass:.2e} kg, Speed: {speed_kmh:.2e} km/h, Energy: {energy:.2e} J")
        return results

    def display_micro_particles_as_table(self, results):
        print("Debug: Displaying micro-particle results as a table.")
        df = pd.DataFrame(results, columns=["Particle", "Mass (kg)", "Speed (km/h)", "Energy (J)"])
        print(df.to_string(index=False))
        return df

    def save_micro_particle_table_as_image(self, df, filename="micro_particles_table_image.png"):
        print("Debug: Saving micro-particle table as an image.")
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.axis('tight')
        ax.axis('off')
        table(ax, df, loc='center', cellLoc='center')
        plt.savefig(filename, bbox_inches='tight')
        print(f"Micro-particle table saved as {filename}.")


def main():
    try:
        print("Debug: Starting main function.")
        time_travel = TimeTravelResearch()

        print("Debug: Calculating for micro-particles (proton, neutron, electron, muon, neutrino).")
        micro_results = time_travel.calculate_micro_particles()

        print("Debug: Displaying micro-particle results as a table.")
        micro_df = time_travel.display_micro_particles_as_table(micro_results)

        print("Debug: Saving micro-particle table as an image.")
        time_travel.save_micro_particle_table_as_image(micro_df)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
