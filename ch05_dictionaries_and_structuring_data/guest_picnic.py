all_guests = {"Alice": {"apples": 5, "pretzels": 12}, "Bob":{"apples": 3, "ham":5 }}

def numbers_off_picnic_iteams(guests, item):
    num_bring_staff = 0
    for k,v in guests.items():
        print(v)
        num_bring_staff += v.get(item, 0)
        print(num_bring_staff)

    return num_bring_staff



numbers_off_picnic_iteams(all_guests, "apples")