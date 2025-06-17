with open('provinces.txt', "rt") as prov:
    provinces_list = []

    for line in prov:
        cleaned = line.strip()

        if cleaned != "":
            if cleaned == "AB":
                cleaned = "Alberta"

            provinces_list.append(cleaned)
    
    provinces_list.pop(0)
    provinces_list.pop()

    alberta_count = provinces_list.count("Alberta")

    print (provinces_list)
    print ()
    print (f"Alberta occurs {alberta_count} times in the modified list.")