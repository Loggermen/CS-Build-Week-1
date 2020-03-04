from random import sample, randint

prefixes =['crystalline','abhorrent','amatory','arcadian','baleful','bilious','dowdy',
            'effulgent','ethereal','execrable','jejune','languid','limpid','luminous',
            'munificent','mordant','minatory','noxious','picayune','serpentine',
            'spurious','tawdry','trenchant','turgid','verdant','wistful']
suffixes =['hall','waste','expanse','turf','reach','cellar','attic','chamber',
            'parlor','portico','vestibulum','tablinum','triclinium','culina',
            'latrina','lararium','cubiculum','taberna','peristylum','lounge',
            'commode',]
latin_nouns = ['pulchitudo','mutatio','misericordia','patria','fortitudo','pertinacia',
            'tellus','fama','familia','fatum','fides','ignis','ignoscentia','amicitia',
            'deus','focus','spes','glacies','gaudium','rex','scientia','vita','lux',
            'amor','memoria','nomen','pax','mare','constantia','gladius','veritas',
            'ultio','virtus','aqua','ventus','verbum','victoria']
latin_verbs = ['amat','vocat','elegit','juvat','defendit']
latin_objects = ['me','nos','amantes','fideles','fortis','sapientes']




def name_gen():
    room_name = ' '.join(sample(prefixes, k=1) + sample(suffixes, k=1))
    return room_name.title

def description_gen():
    description_1 = sample(latin_nouns, k=1) + sample(latin_nouns, k=1)
    description_2 = sample(latin_nouns, k=1)
    description_3 = sample(latin_nouns, k=1) + sample(latin_objects, k=1) +sample(latin_verbs, k=1)
    num = randint(1,5)
    if num == 1:
        return ' et '.join(description_1)
    elif num == 2:
        return ''.join(description_2)+', '+' et '.join(description_1)
    elif num == 3:
        return 'Ex '+' '.join(description_1)
    elif num == 4:
        return ' '.join(description_3)
    else:
        return 'In '+' '.join(description_1)
