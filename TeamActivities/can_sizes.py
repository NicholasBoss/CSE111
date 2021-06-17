"""
Team 1B Activity # 3

can_sizes.py
"""
from math import pi
    
def main():
    with open("can_size.csv") as can_file:
        can_file.readline()
        efficency = []
        can_name = []
        storage_efficiencies = []
        for line in can_file:
            line = line.strip()
            line = line.split(',')

            name = line[0]
            radius = float(line[1])
            height = float(line[2])
            cost_per_can = float(line[3])

            volume = cylinder_volume(radius,height)

            surface_area = cylinder_surface_area(radius,height)

            storage_efficiency = cylinder_storage_efficiency(volume,surface_area)

            cost_efficiency = cylinder_cost_efficency(volume, cost_per_can)

            efficency.append(cost_efficiency)

            can_name.append(name)

            storage_efficiencies.append(storage_efficiency)

            print(f"{name}, {storage_efficiency:.1f}, {cost_efficiency:.0f}")

        index = efficency.index(max(efficency))
        index1 = storage_efficiencies.index(max(storage_efficiencies))
        print(f"The max efficent cost is: ${max(efficency):.0f} as the {can_name[index]} can.")
        print(f"The max storage efficent can is: {can_name[index1]}")

            

def cylinder_volume(radius,height):
    volume = pi * radius**2  * height
    return volume

def cylinder_surface_area(radius,height):
    surface_area = 2*pi * radius*(radius + height)
    return surface_area

def cylinder_storage_efficiency(volume,surface_area):
    storage_efficiency = volume / surface_area
    return storage_efficiency

def cylinder_cost_efficency(volume, cost_per_can):
    cost_efficiency = volume / cost_per_can
    return cost_efficiency
main()