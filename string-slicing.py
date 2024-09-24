#slicing = create a substring by extrancting elements from another string
#          indexing[] or slice()
#          [start:stop:slice]

name = "Ozge Eser"

first_name = name[0]
sliced_name = name[:4] #Instead of writing [0:4] you could write: [:4] 
last_name = name[5:] #Instead of writing [5:10] you could write: [5:] 
funky_name = name[0:10:2]
reversed_name = name[::-1]

print(first_name)
print(sliced_name)
print(last_name)
print(funky_name)
print(reversed_name)

website = "https://eserozge.com/"

slice = slice(8,-5)

website[slice]

print(website[slice])