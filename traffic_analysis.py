def calculate_signal_time(vehicle_count):
    if vehicle_count < 10:
        return 15   # seconds
    elif vehicle_count < 30:
        return 30
    else:
        return 60


def traffic_status(vehicle_count):
    if vehicle_count < 10:
        return "Low Traffic"
    elif vehicle_count < 30:
        return "Medium Traffic"
    else:
        return "High Traffic"


def simulate_signal(vehicle_count):
    status = traffic_status(vehicle_count)
    time = calculate_signal_time(vehicle_count)

    print("Traffic Status:", status)
    print("Green Signal Time:", time, "seconds")


# Example run
if __name__ == "__main__":
    count = int(input("Enter number of vehicles: "))
    simulate_signal(count)
