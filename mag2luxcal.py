import numpy as np


def mag2fluxcal_SNANA(mag, mag_err):
    """ Conversion from magnitude to Fluxcal
        from SNANA manual
        Error: derivative of fluxcal=10**(11-.4m)
    Args: 
        mag
        mag_err
    Out: 
        fluxcal 
        fluxcal_err : absolute error (the derivative has a minus sign)
    
    """
    if mag == None:
        return None, None
    fluxcal = 10 ** (-0.4 * mag) * 10 ** (11)
    fluxcal_err = 9.21034 * 10 ** 10 * np.exp(-0.921034 * mag) * mag_err

    return fluxcal, fluxcal_err
    
"""Usage
"""
mag = 22
mag_err = 2.4
fluxcal, fluxcal_err = mag2fluxcal_SNANA(mag, mag_err)
