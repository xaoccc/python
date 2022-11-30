country = input()
device = input()
 
if country == "Russia":
    if device == "ribbon":
        hard = 9.100
        perf = 9.400
    elif device == "hoop":
        hard = 9.300
        perf = 9.800
    elif device == "rope":
        hard = 9.600
        perf = 9.000
elif country == "Bulgaria":
    if device == "ribbon":
        hard = 9.600
        perf = 9.400
    elif device == "hoop":
        hard = 9.550
        perf = 9.750
    elif device == "rope":
        hard = 9.500
        perf = 9.400
elif country == "Italy":
    if device == "ribbon":
        hard = 9.200
        perf = 9.500
    elif device == "hoop":
        hard = 9.450
        perf = 9.350
    elif device == "rope":
        hard = 9.700
        perf = 9.150
total_score = hard + perf
print(f"The team of {country} get {total_score:.3f} on {device}.")
print(f"{((20 - total_score) * 100 / 20):.2f}%")
