import csv

def check_repeats(name_list, album):
    copies = {}
    for name in name_list:
        album_counter = []
        counter = 0
        item_counter = 0
        for name2 in name_list:
            if name == name2:
                counter += 1
                album_counter.append(album[item_counter])
                print(name + " worked on " + album[item_counter])
                # else:
                #     print("Same row")
            # else:
                # print("Not the same")
            item_counter += 1
        if len(album_counter) > 1:
            copies[name] = album_counter
    return copies
        
def check_final():
    with open('engineers.csv', newline='') as read_obj:
        # pass the file object to reader() to get the reader object
        reader = csv.DictReader(read_obj)

        names = []
        albums = []
        for row in reader:
            names.append(row['Name'])
            albums.append(row['Credits'])
        
        return check_repeats(names, albums)


def print_final_csv(name_and_album_dict):
    with open('final.csv', mode='w', newline='') as read_obj:
        # pass the file object to reader() to get the reader object
        fieldnames = ['Name', 'Album']
        writer = csv.DictWriter(read_obj, fieldnames = fieldnames)
        writer.writeheader()

        people = []
        albums = []
        for name in name_and_album_dict.keys():
            people.append(name)
            albums.append(name_and_album_dict[name])

        for (person, album) in zip(people, albums):
            write_row_dict = {}
            write_row_dict['Name'] = person
            write_row_dict['Album'] = album

            writer.writerow(write_row_dict)
        


print(check_final())
print_final_csv(check_final())