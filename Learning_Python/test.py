family_names = []
i = 0
print(family_names)
while i <= 3 :
  name = input("whats the name ? ")
  family_names.append(name)
  i += 1
i=0
while i<= 3 :
  print("\t" + "Family name %d: "%i + family_names[i])
  i+=1
print("That's AMAZING !!! :)")

print("\nWho left ? - options(0, 1, 2 or 3)")
this_person_left = input("It was option ")
if this_person_left != str(0) and this_person_left != str(1) and this_person_left != str(2) and this_person_left!= str(3) :
    print("It seems that you don't know...")
else :
    print("How pity! " + family_names.pop(int(this_person_left)) + " left !")
