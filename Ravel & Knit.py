#NOMOR 3
'''
fungsi ravel harus mengurai perhuruf dari kata diprint bertingkat
fungsi knit harus menyatukan kata dari uraian bertingkat
'''

kata = input("masukkan kata : ")

def ravel (r):
    list_1 = []
    uraian = ""
    for i in r :
        uraian+=i
        list_1.append(uraian)
    return "".join(list_1)

print(ravel(kata))

def knit (r):
    list_2 = []
    pemisah = r[((len(r)-1)//3):(len(r)-1)] 
    list_2.append(pemisah)
    return list_2



print(knit(kata))