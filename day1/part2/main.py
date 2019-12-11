from day1.main import calculate_fuel_number

def calculate_additional_fuel(original_fuel):
    total_fuel = 0
    previous_fuel = original_fuel
    while not previous_fuel <= 0:
        fuel = calculate_fuel_number(previous_fuel)
        if fuel < 0:
            return total_fuel
        else:
            total_fuel += fuel
            previous_fuel = fuel
            print(fuel)
    return total_fuel




if __name__ == "__main__":
    with open("input.txt", "r") as mass_input:
        final_fuel_requirements = 0
        for line in mass_input.readlines():
            print(f'Mass: {line}')
            pre_fuel = calculate_fuel_number(int(line))
            print(f'Pre-fuel: {pre_fuel}')
            additional_fuel = calculate_additional_fuel(pre_fuel)
            print(f'Additional fuel: {additional_fuel}')
            final_fuel_requirements += pre_fuel
            final_fuel_requirements += additional_fuel
            print(f"Total Fuel: {pre_fuel+additional_fuel}")
        print(f'Final Fuel Requirements: {final_fuel_requirements}')
