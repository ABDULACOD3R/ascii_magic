import  os 
os.system("clear ;pkg install jp2a ;clear")
s= '''
              c0000000Oc
              Cdlkk0000O
         .oxxxxxxxx0000O kkd'
        .0KKK0000000000d 0KK0.
        ,KKKKOllooooooll00KKK,
        .0KKK oxxkkkOOO000KK0.
         .oxx xxxkkooooddddc.
              xxxkkxkld
              Cdxkkkkc0o
'''
print(s)
print("========image==to==text============")
file=input("[ Path ] File ? >> ")
print("==============zed==================")
os.system("jp2a "+file)
