# Here is where all the equations that are used are defined

# def current_density_eq(v,i,a,d):
#     current_density=[]
#     for voltage,current in zip(v, i):
#         if voltage or current ==0:
#             current_density.append(None)
#             continue
#         new_num= (d / ((voltage / current) * a**2)) * (voltage / d)
# if new num gives invalde num retun 0
#         print(current_density)
#         current_density.append(new_num)
#     return current_density

def weird_division(n, d):
    return n / d if d else 0


def zero_devision_check(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return 0

def current_density_eq(v,i,a,d):
    current_density=[]
    for voltage,current in zip(v, i):
        if voltage == 0 or current == 0:
            current_density.append(0)
            # for checking for divide by zero error
            continue
        new_num = (d / ((voltage / current) * a ** 2)) * (voltage / d)
        current_density.append(new_num)
    return current_density

def electric_field_eq(v,d):
    electric_field=[]
    for voltage in v:
        if voltage == 0:
            electric_field.append(0)
            continue
        new_num= voltage/d
        electric_field.append(new_num)
    return electric_field

def current_over_voltage_eq(v,i):
    current_over_voltage=[]
    for voltage,current in zip (v,i):
        if voltage == 0 or current == 0:
            current_over_voltage.append(0)
            # for checking for divide by zero error
            continue
        new_num= current/voltage
        current_over_voltage.append(new_num)
    return current_over_voltage

def voltage_to_the_half_eq(v):
    voltage_to_the_half=[]
    for voltage in v:
        new_num= voltage**1/2
        voltage_to_the_half.append(new_num)
    return voltage_to_the_half
