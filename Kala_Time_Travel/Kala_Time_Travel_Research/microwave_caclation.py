import math


def calculate_frequency(wavelength):
    """
    Calculate the frequency of a microwave given its wavelength.
    :param wavelength: Wavelength in meters (m).
    :return: Frequency in hertz (Hz).
    """
    c = 3e8  # Speed of light in m/s
    frequency = c / wavelength
    return frequency


def calculate_energy(wavelength):
    """
    Calculate the energy of a microwave photon given its wavelength.
    :param wavelength: Wavelength in meters (m).
    :return: Energy in joules (J).
    """
    h = 6.626e-34  # Planck's constant in Js
    c = 3e8  # Speed of light in m/s
    energy = (h * c) / wavelength
    return energy


def calculate_momentum(energy):
    """
    Calculate the momentum of a microwave photon given its energy.
    :param energy: Energy in joules (J).
    :return: Momentum in kg·m/s.
    """
    c = 3e8  # Speed of light in m/s
    momentum = energy / c
    return momentum


def main():
    print("Microwave Properties Calculator")

    # Input wavelength in meters
    wavelength = float(input("Enter the wavelength of the microwave (in meters): "))

    # Perform calculations
    frequency = calculate_frequency(wavelength)
    energy = calculate_energy(wavelength)
    momentum = calculate_momentum(energy)

    # Display results
    print(f"\nResults for Wavelength: {wavelength} meters")
    print(f"Frequency: {frequency:.2e} Hz")
    print(f"Energy: {energy:.2e} J")
    print(f"Momentum: {momentum:.2e} kg·m/s")


if __name__ == "__main__":
    main()
