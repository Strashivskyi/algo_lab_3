def string_to_people(input_string):
    input_string = input_string.split(" ")
    people = []
    if len(input_string) > 50:
        raise Exception('The input data includes too many people')
    else:
        for person in range(len(input_string)):
            people.append([])
            if len(input_string[person]) > 50:
                raise Exception('The data is not appropriate. Number of beers for each person is too big')
            else:
                for beer in range(len(input_string[person])):
                    if input_string[person][beer] == "Y":
                        people[person].append(beer + 1)
            
    return people