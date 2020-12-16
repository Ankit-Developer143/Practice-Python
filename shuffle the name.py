def name_shuffle(txt):
    val =txt.split()[::-1]
    return " ".join(val)
    
print(name_shuffle("Rosie O'Donnell"))