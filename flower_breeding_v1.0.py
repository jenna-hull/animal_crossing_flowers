
# we want a full list of all ova that can be created from a single parent
# this means we want the list of 1 vs 2 for each position
# over the list of all possible ova, combine them with the other parent
# identify what color the baby is

roses = { 'rryyWWss': 'White',
    'rryyWWss': 'White',
    'rryyWWSS': 'White',
    'rryyWwss': 'White',
    'rryyWwSs': 'White',
    'rryyWwSS': 'White',
    'rryywwss': 'Purple',
    'rryywwSs': 'Purple',
    'rryywwSS': 'Purple',
    'rrYyWWss': 'Yellow',
    'rrYyWWSs': 'Yellow',
    'rrYyWWSS': 'Yellow',
    'rrYyWwss': 'White',
    'rrYyWwSs': 'White',
    'rrYyWwSS': 'White',
    'rrYywwss': 'Purple',
    'rrYywwSs': 'Purple',
    'rrYywwSS': 'Purple',
    'rrYYWWss': 'Yellow',
    'rrYYWWSs': 'Yellow',
    'rrYYWWSS': 'Yellow',
    'rrYYWwss': 'Yellow',
    'rrYYWwSs': 'Yellow',
    'rrYYWwSS': 'Yellow',
    'rrYYwwss': 'White',
    'rrYYwwSs': 'White',
    'rrYYwwSS': 'White',
    'RryyWWss': 'Red',
    'RryyWWSs': 'Pink',
    'RryyWWSS': 'White',
    'RryyWwss': 'Red',
    'RryyWwSs': 'Pink',
    'RryyWwSS': 'White',
    'Rryywwss': 'Red',
    'RryywwSs': 'Pink',
    'RryywwSS': 'Purple',
    'RrYyWWss': 'Orange',
    'RrYyWWSs': 'Yellow',
    'RrYyWWSS': 'Yellow',
    'RrYyWwss': 'Red',
    'RrYyWwSs': 'Pink',
    'RrYyWwSS': 'White',
    'RrYywwss': 'Red',
    'RrYywwSs': 'Pink',
    'RrYywwSS': 'Purple',
    'RrYYWWss': 'Orange',
    'RrYYWWSs': 'Yellow',
    'RrYYWWSS': 'Yellow',
    'RrYYWwss': 'Orange',
    'RrYYWwSs': 'Yellow',
    'RrYYWwSS': 'Yellow',
    'RrYYwwss': 'Red',
    'RrYYwwSs': 'Pink',
    'RrYYwwSS': 'White',
    'RRyyWWss': 'Black',
    'RRyyWWSs': 'Red',
    'RRyyWWSS': 'Pink',
    'RRyyWwss': 'Black',
    'RRyyWwSs': 'Red',
    'RRyyWwSS': 'Pink',
    'RRyywwss': 'Black',
    'RRyywwSs': 'Red',
    'RRyywwSS': 'Pink',
    'RRYyWWss': 'Orange',
    'RRYyWWSs': 'Orange',
    'RRYyWWSS': 'Yellow',
    'RRYyWwss': 'Red',
    'RRYyWwSs': 'Red',
    'RRYyWwSS': 'White',
    'RRYywwss': 'Black',
    'RRYywwSs': 'Red',
    'RRYywwSS': 'Purple',
    'RRYYWWss': 'Orange',
    'RRYYWWSs': 'Orange',
    'RRYYWWSS': 'Yellow',
    'RRYYWwss': 'Orange',
    'RRYYWwSs': 'Orange',
    'RRYYWwSS': 'Yellow',
    'RRYYwwss': 'Blue',
    'RRYYwwSs': 'Red',
    'RRYYwwSS': 'White'
}

cosmos = {'rryyss': 'White',
'rryySs': 'White',
'rryySS': 'White',
'rrYyss': 'Yellow',
'rrYySs': 'Yellow',
'rrYySS': 'White',
'rrYYss': 'Yellow',
'rrYYSs': 'Yellow',
'rrYYSS': 'Yellow',
'Rryyss': 'Pink',
'RryySs': 'Pink',
'RryySS': 'Pink',
'RrYyss': 'Orange',
'RrYySs': 'Orange',
'RrYySS': 'Pink',
'RrYYss': 'Orange',
'RrYYSs': 'Orange',
'RrYYSS': 'Orange',
'RRyyss': 'Red',
'RRyySs': 'Red',
'RRyySS': 'Red',
'RRYyss': 'Orange',
'RRYySs': 'Orange',
'RRYySS': 'Red',
'RRYYss': 'Black',
'RRYYSs': 'Black',
'RRYYSS': 'Red'
}

lilies = {
    'rryyss' :'White',
    'rryySs' :'White',
    'rryySS' :'White',
    'rrYyss' :'Yellow',
    'rrYySs' :'White',
    'rrYySS' :'White',
    'rrYYss' :'Yellow',
    'rrYYSs' :'Yellow',
    'rrYYSS' :'White',
    'Rryyss' :'Red',
    'RryySs' :'Pink',
    'RryySS' :'White',
    'RrYyss' :'Orange',
    'RrYySs' :'Yellow',
    'RrYySS' :'Yellow',
    'RrYYss' :'Orange',
    'RrYYSs' :'Yellow',
    'RrYYSS' :'Yellow',
    'RRyyss' :'Black',
    'RRyySs' :'Red',
    'RRyySS' :'Pink',
    'RRYyss' :'Black',
    'RRYySs' :'Red',
    'RRYySS' :'Pink',
    'RRYYss' :'Orange',
    'RRYYSs' :'Orange',
    'RRYYSS' :'White'
}

pansies = {
    'rryyWW' : 'White',
    'rryyWw' : 'White',
    'rryyww' : 'Blue',
    'rrYyWW' : 'Yellow',
    'rrYyWw' : 'Yellow',
    'rrYyww' : 'Blue',
    'rrYYWW' : 'Yellow',
    'rrYYWw' : 'Yellow',
    'rrYYww' : 'Yellow',
    'RryyWW' : 'Red',
    'RryyWw' : 'Red',
    'Rryyww' : 'Blue',
    'RrYyWW' : 'Orange',
    'RrYyWw' : 'Orange',
    'RrYyww' : 'Orange',
    'RrYYWW' : 'Yellow',
    'RrYYWw' : 'Yellow',
    'RrYYww' : 'Yellow',
    'RRyyWW' : 'Red',
    'RRyyWw' : 'Red',
    'RRyyww' : 'Purple',
    'RRYyWW' : 'Red',
    'RRYyWw' : 'Red',
    'RRYyww' : 'Purple',
    'RRYYWW' : 'Orange',
    'RRYYWw' : 'Orange',
    'RRYYww' : 'Purple'
}

hyacinths = {
    'rryyWW' : 'White',
    'rryyWw' : 'White',
    'rryyww' : 'Blue',
    'rrYyWW' : 'Yellow',
    'rrYyWw' : 'Yellow',
    'rrYyww' : 'White',
    'rrYYWW' : 'Yellow',
    'rrYYWw' : 'Yellow',
    'rrYYww' : 'Yellow',
    'RryyWW' : 'Red',
    'RryyWw' : 'Pink',
    'Rryyww' : 'White',
    'RrYyWW' : 'Orange',
    'RrYyWw' : 'Yellow',
    'RrYyww' : 'Yellow',
    'RrYYWW' : 'Orange',
    'RrYYWw' : 'Yellow',
    'RrYYww' : 'Yellow',
    'RRyyWW' : 'Red',
    'RRyyWw' : 'Red',
    'RRyyww' : 'Red',
    'RRYyWW' : 'Blue',
    'RRYyWw' : 'Red',
    'RRYyww' : 'Red',
    'RRYYWW' : 'Purple',
    'RRYYWw' : 'Purple',
    'RRYYww' : 'Purple'
}

tulips = {
    'rryyss': 'White',
    'rryySs': 'White',
    'rryySS': 'White',
    'rrYyss': 'Yellow',
    'rrYySs': 'Yellow',
    'rrYySS': 'White',
    'rrYYss': 'Yellow',
    'rrYYSs': 'Yellow',
    'rrYYSS': 'Yellow',
    'Rryyss': 'Red',
    'RryySs': 'Pink',
    'RryySS': 'White',
    'RrYyss': 'Orange',
    'RrYySs': 'Yellow',
    'RrYySS': 'Yellow',
    'RrYYss': 'Orange',
    'RrYYSs': 'Yellow',
    'RrYYSS': 'Yellow',
    'RRyyss': 'Black',
    'RRyySs': 'Red',
    'RRyySS': 'Red',
    'RRYyss': 'Black',
    'RRYySs': 'Red',
    'RRYySS': 'Red',
    'RRYYss': 'Purple',
    'RRYYSs': 'Purple',
    'RRYYSS': 'Purple'
}

mums = {
    'rryyWW': 'White',
    'rryyWw': 'White',
    'rryyww': 'Purple',
    'rrYyWW': 'Yellow',
    'rrYyWw': 'Yellow',
    'rrYyww': 'White',
    'rrYYWW': 'Yellow',
    'rrYYWw': 'Yellow',
    'rrYYww': 'Yellow',
    'RryyWW': 'Pink',
    'RryyWw': 'Pink',
    'Rryyww': 'Pink',
    'RrYyWW': 'Yellow',
    'RrYyWw': 'Red',
    'RrYyww': 'Pink',
    'RrYYWW': 'Purple',
    'RrYYWw': 'Purple',
    'RrYYww': 'Purple',
    'RRyyWW': 'Red',
    'RRyyWw': 'Red',
    'RRyyww': 'Red',
    'RRYyWW': 'Purple',
    'RRYyWw': 'Purple',
    'RRYyww': 'Red',
    'RRYYWW': 'Green',
    'RRYYWw': 'Green',
    'RRYYww': 'Red'
}

windflower = {
    'rrooWW': 'White',
    'rrooWw': 'White',
    'rrooww': 'Blue',
    'rrOoWW': 'Orange',
    'rrOoWw': 'Orange',
    'rrOoww': 'Blue',
    'rrOOWW': 'Orange',
    'rrOOWw': 'Orange',
    'rrOOww': 'Orange',
    'RrooWW': 'Red',
    'RrooWw': 'Red',
    'Rrooww': 'Blue',
    'RrOoWW': 'Pink',
    'RrOoWw': 'Pink',
    'RrOoww': 'Pink',
    'RrOOWW': 'Orange',
    'RrOOWw': 'Orange',
    'RrOOww': 'Orange',
    'RRooWW': 'Red',
    'RRooWw': 'Red',
    'RRooww': 'Purple',
    'RROoWW': 'Red',
    'RROoWw': 'Red',
    'RROoww': 'Purple',
    'RROOWW': 'Pink',
    'RROOWw': 'Pink',
    'RROOww': 'Purple'
}

def generate_all_3_indeces():
    indeces = set()
    h = 0
    i = 1
    j = 1
    k = 1
    genome = [0,0,0]
    while h < 1:
        while i < 3:
            genome[0] = i
            i = i + 1
            j = 1
            while j < 3:
                genome[1] = j
                j = j + 1
                k = 1
                while k < 3:
                    genome[2] = k
                    indeces.add(str(genome))
                    k = k + 1
        h = h + 1
    return(indeces)


def generate_all_4_indeces():
    indeces = set()
    h = 0
    i = 1
    j = 1
    k = 1
    m = 1
    genome = [0, 0, 0, 0]
    while h < 1:
        while i < 3:
            genome[0] = i
            i = i + 1
            j = 1
            while j < 3:
                genome[1] = j
                j = j + 1
                k = 1
                while k < 3:
                    genome[2] = k
                    k = k + 1
                    m = 1
                    while m < 3:
                        genome[3] = m
                        indeces.add(str(genome))
                        m = m + 1
        h = h + 1
    return(indeces)

#need to correctly meiosis - not selecting the correct genes from the genotype
def parentMeiosis(genotype, indeces): #where genotype is the full 6 or 8 gene series & index is the 1 or 2 from each pair
    #that should be selected
    ova = []
    sublist = []
    allele_pairs = len(genotype)/2 #is this a 3 pair or 4 pair flower?
    pairs = 0
    while pairs < allele_pairs: #treat 2 genes together as a pair, and iterate through the number of pairs ther are
        sublist = genotype[(pairs*2):((pairs*2)+2)] #look only at 0-1, 2-3, etc
        index_to_find = (pairs/2)
        found_index = indeces[index_to_find]
        found_index = int(found_index) - 1
        sublist[found_index]
        gene = sublist[found_index]
        ova.append(gene) #add the gene
        pairs = pairs + 1 #increment
    return ova


def breed(ovaA, ovaB):
    child = []
    for gene in ovaA:
        index = ovaA.index(gene)
        if ovaA[index].isupper():
                child.append(ovaA[index])
                child.append(ovaB[index])
        else:
            child.append(ovaB[index])
            child.append(ovaA[index])
    child_string = ''
    for entry in child:
        child_string = child_string + entry
    return child_string


def identify_color(species, genotype):
    phenotype = species.get(genotype)
    return phenotype


def possibleOffspring(parentA, parentB, species):
    if species == 'rose':
        aIndeces = generate_all_4_indeces()
        bIndeces = generate_all_4_indeces()
    else:
        aIndeces = generate_all_3_indeces()
        bIndeces = generate_all_3_indeces()
    aIndeces = list(aIndeces)
    bIndeces = list(bIndeces)
    aOvum = []
    bOvum = []
    for index in aIndeces:
        index = list(index)
        index = index[1::3]
        aOvum.append(parentMeiosis(parentA, index))
    for index in bIndeces:
        index = list(index)
        index = index[1::3]
        bOvum.append(parentMeiosis(parentB, index))

    children = []
    for aEgg in aOvum:
        for bEgg in bOvum:
            breed(aEgg, bEgg)
            children.append(breed(aEgg, bEgg))
    return children

