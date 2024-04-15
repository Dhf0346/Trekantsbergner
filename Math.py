import math
# tak til Mikkel fra 1.r for at hjælpe med det her regner.


def pythagoras_hypotenuse(a, b):
    svar = math.sqrt(a**2+b**2)
    return svar


def pythagoras_katete(a, c):
    svar = math.sqrt(c**2-a**2)
    return svar


def cosinus_katete_ret(v, c):
    svar = math.cos(math.radians(v))*c
    return svar


def sinus_katete_ret(v, c):
    svar = math.sin(math.radians(v))*c
    return svar


def tangens_modkatete_ret(v, a):
    svar = math.tan(math.radians(v))*a
    return svar


def tangens_hoskatete_ret(v, b):
    svar = b/math.tan(math.radians(v))
    return svar


def sinus_hypoteenuse_ret(v, side):
    svar = side/math.sin(math.radians(v))
    return svar


def cosinus_hypoteenuse_ret(v, side):
    svar = side/math.cos(math.radians(v))
    return svar


def sinus_vinkel_ret(a, c):
    svar = math.degrees(math.asin(a/c))
    return svar


def cosinus_vinkel_ret(b, c):
    svar = math.degrees(math.acos(b/c))
    return svar


def tangens_vinkel_ret(a, b):
    svar = math.degrees(math.atan(a/b))
    return svar


def vinkelsum(vinkel1, vinkel2):
    svar = 180 - (vinkel1+vinkel2)
    return svar


def cosinusrelation_side_vil(side1, side2, vinkel):
    svar = math.sqrt(side1**2+side2**2-2*side1*side2*math.cos(math.radians(vinkel)))
    return svar


def sinusrelation_side_vil(side, vinkel, vinkel1):
    svar = (side*math.sin(math.radians(vinkel1)))/math.sin(math.radians(vinkel))
    return svar


def cosinusrelationVinkelA(side1, side2, side3):
    svar = math.degrees(math.acos((side2**2+side3**2-side1**2)/(2*side2*side3)))
    return svar


def cosinusrelationVinkelB(side1, side2, side3):
    svar = math.degrees(math.acos((side1**2 + side3**2 - side2**2)/(2*side1*side3)))
    return svar


def sinusrelation_vinkel_vil(side1, side2, vinkel):
    svar = math.degrees(math.asin((side1*math.sin(math.radians(vinkel)))/side2))
    return svar
