def water_column_height(tower_height, tank_height):
    """
    Calculates and returns the height of a water column.

    Parameters: tower height, tank height
    Return: water column height
    """

    water_column_height = tower_height + (3 * tank_height / 4)
    return water_column_height

def pressure_gain_from_water_height(height, water_density=998.2, gravity=9.80665):
    """
    Calculates and returns water pressure in kilopascals based on water height.

    Parameters: height of the water column in meters, water density, rate of gravity
    Return: water pressue in kilopascals 
    """
    pressure = water_density * gravity * height / 1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity, water_density=998.2):
    """
    Calculates and returns water pressure lost because of the friction between the water and the walls of a pipe that it flows through.

    Paramters: pipe diameter (in meters), pipe length (in meters), friction factor, water density, fluid velocity (in meters per second)
    Return: pressure loss in kilopascals
    """
    pressure_loss = -friction_factor * pipe_length * water_density * fluid_velocity ** 2 / (2000 * pipe_diameter)
    return pressure_loss

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings, water_density=998.2):
    """ 
    Calculates and returns water pressure lost because of fittings such as 45 and 90 degree bends that are in a pipeline.

    Params: fluid velocity (in meters/second), quantity of fittings, and density of water (in kilograms/meter cubed)
    Return: lost_pressure
    """
    lost_pressure = -0.04 * water_density * fluid_velocity ** 2 * quantity_fittings / 2000
    return lost_pressure

def reynolds_number(hydraulic_diameter, fluid_velocity, water_density=998.2, dynamic_viscosity=0.0010016):
    reynolds_number = water_density * hydraulic_diameter * fluid_velocity / dynamic_viscosity
    return reynolds_number

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter, water_density=998.2):
    k = (0.1 + 50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    pressure_lost = -k * water_density * fluid_velocity ** 2 / 2000
    return pressure_lost


PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)

dynamic_viscosity_of_water = 0.0010016 # in Pascal seconds
water_density = 998.2 # in kilograms/meter^3
earth_acceleration_of_gravity = 9.80665 # in something, I don't know


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")


if __name__ == "__main__":
    main()