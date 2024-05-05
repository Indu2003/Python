def estimated_cost(in_walls, ext_walls, in_surfarea, ext_surfarea):
    int_surf = in_walls * sum(in_surfarea)  # Summing up all surface areas for interior walls
    ext_surf = ext_walls * sum(ext_surfarea)  # Summing up all surface areas for exterior walls
    tot_surf = int_surf + ext_surf
    total_cost = tot_surf * 3.15
    return total_cost

in_walls = int(input("Enter number of interior walls: "))
ext_walls = int(input("Enter number of exterior walls: "))

in_surfarea_str = input("Enter the surface area of each interior wall in square feet separated by spaces: ")
in_surfarea = [float(area) for area in in_surfarea_str.split()]

ext_surfarea_str = input("Enter the surface area of each exterior wall in square feet separated by spaces: ")
ext_surfarea = [float(area) for area in ext_surfarea_str.split()]

estimated_cost_value = estimated_cost(in_walls, ext_walls, in_surfarea, ext_surfarea)
print("Estimated cost for painting:", estimated_cost_value)
