def kepler_third_time_from_semimajor(semimajor_axis):
    # Returns the orbital period based on semimajor axis using Kepler's Third Law
    orbital_period = (semimajor_axis**3)**0.5
    return orbital_period