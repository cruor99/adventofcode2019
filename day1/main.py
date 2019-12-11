import math

def calculate_fuel_number(mass):
    fuel_number = math.floor(mass/3) - 2
    return fuel_number


if __name__ == "__main__":
    with open("input.txt", "r") as mass_input:
        final_fuel_score = 0
        for line in mass_input.readlines():
            print(line)
            fuel_number = calculate_fuel_number(int(line))
            final_fuel_score += fuel_number
        print(f'Final Fuel Score: {final_fuel_score}')

