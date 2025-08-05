"""Fileban lévő tanulók vagy szavak rendezése"""





# Functions

# Variables
txt_data_input = input("Add meg az adatok betöltésére szolgáló file nevét: ")

txt_data = open(txt_data_input, "r", encoding="utf8")

students = []

sorted_list = []

# Program

# Betöltöm a szöveges fileban felsorolt szavakat/tanulókat és listába rendezem
# (egy sorba egy szó vagy egy személy neve van.)
while 1:
    read_txt = txt_data.readline()
    if read_txt == "" or read_txt == "\n":
        break
    t = read_txt.strip("\n")
    students.append(t)

# Minden elemet egyesével vizsgálok meg.
for name in students:
    # i újrainicializálása
    i = 0

    # sorted_list hosszának újraszámolása
    length_sorted_list = len(sorted_list)

    # Itt megvizsgálom, hogy milyen hosszú a sorted_list és addig fut amíg kisebb vagy egyenlő i-vel.
    while i <= length_sorted_list:

        # Ha üres a lista, adja hozzá az elemet.
        if length_sorted_list == 0:
            sorted_list.append(name)
            break

        # Ha nem üres a lista akkor... A listát a végéről kezdi el ellenőrizni a - előjel miatt.
        elif length_sorted_list > 0:

            # Ha a name értéke kisebb mint a sorted list eleme akkor,
            if name < sorted_list[-i]:

                # Ha i = a sortedlist hosszával, akkor a lista 0. eleménél járunk, ez elé fogja betenni.
                if i == length_sorted_list:
                    sorted_list[-i:-i] = [name]
                    break

                # Ha -i -1. eleme nagyobb mint a name, de kisebb mint a -i. elem, akkor a -i indexre helyezem az elemet.
                # Az egyenlőség azért kell, ha ugyanaz a szó többször szerepel a listában.
                elif sorted_list[-i - 1] <= name <= sorted_list[-i]:
                    sorted_list[-i:-i] = [name]
                    break

        # Léptetés
        i += 1

print(sorted_list)
