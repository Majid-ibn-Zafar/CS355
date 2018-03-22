import numpy as np

ONE_MINUTE = 1.0/60.0
STRANDED = -1


def simulate_flight_a():

    a_to_b = 8.0 + np.random.normal(4, 0.25)

    if 12.5 - a_to_b >= ONE_MINUTE:
        b_to_c = 12.5
    elif 13.0 - a_to_b >= ONE_MINUTE:
        b_to_c = 13.0
    else:
        return STRANDED

    b_to_c += np.random.normal(4, 0.25)

    if 17.0 - b_to_c >= ONE_MINUTE:
        c_to_d = 17.0
    elif 17.5 - b_to_c >= ONE_MINUTE:
        c_to_d = 17.5
    elif 18.0 - b_to_c >= ONE_MINUTE:
        c_to_d = 18.0
    else:
        return STRANDED

    c_to_d += np.random.normal(3.5, 0.25)
    return c_to_d


def simulate_flight_b():

    a_to_e = 8.0 + np.random.normal(3.5, 0.5)

    if 12.0 - a_to_e >= ONE_MINUTE:
        e_to_f = 12.0
    elif 12.5 - a_to_e >= ONE_MINUTE:
        e_to_f = 12.5
    else:
        return STRANDED

    e_to_f += np.random.normal(4, 0.5)

    if 16.5 - e_to_f >= ONE_MINUTE:
        f_to_d = 16.5
    elif 17.0 - e_to_f >= ONE_MINUTE:
        f_to_d = 17.0
    elif 17.5 - e_to_f >= ONE_MINUTE:
        f_to_d = 17.5
    else:
        return STRANDED

    f_to_d += np.random.normal(3.5, 0.5)
    return f_to_d


def simulate(count):
    avg_arrival_time_a = 0
    avg_arrival_time_b = 0
    stranded_a = 0
    stranded_b = 0

    for _ in range(count):
        a = simulate_flight_a()
        if a is STRANDED:
            stranded_a += 1
        else:
            avg_arrival_time_a += a

        b = simulate_flight_b()
        if b is STRANDED:
            stranded_b += 1
        else:
            avg_arrival_time_b += b

    stranded_a = stranded_a / count
    stranded_b = stranded_b / count
    avg_arrival_time_a = avg_arrival_time_a / count
    avg_arrival_time_b = avg_arrival_time_b / count

    print("Average Arrival Time with Airline A: " + str(int(avg_arrival_time_a)) + ":" +
          str(int(60*(avg_arrival_time_a % 1))))
    print("Percent Stranded with Airline A: " + str(100 * stranded_a) + "%")
    print("Average Arrival Time with Airline B: " + str(int(avg_arrival_time_b)) + ":" +
          str(int(60*(avg_arrival_time_b % 1))))
    print("Percent Stranded with Airline B: " + str(100 * stranded_b) + "%")


simulate(10000)
