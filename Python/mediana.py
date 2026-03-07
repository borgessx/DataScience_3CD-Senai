list = [3,4,5,6,7]
list1 = [3,4,5,6,7,8,9]
list2 =[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list3 = [7,2,3,9,4,11]

def mediana(list):
    list.sort()
    nu = int(len(list)/2)
    print(list[nu])

mediana(list)
mediana(list1)
mediana(list2)
mediana(list3)

