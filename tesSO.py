import re
# Id, priority, lama proses, burst-time, waktu akses I/O, clock awal
namafile = input('masukan nama file : ')
bukaFile = open(namafile,"r")

proses = []

for baris in bukaFile:
    cari = re.findall(r'\d+',baris)
    for isi in cari:
        cari[cari.index(isi)] = int(cari[cari.index(isi)])
    proses.append(cari)

bukaFile.close()

done=0
doneFCFS=0
antrian=[]
antrianFCFS=[[]]
panjang = len(proses)
gT=0
noAntri=1
nomAntri=1

tes=0
print('proses : ')
for baris in proses:
    print(baris)

while(done!=len(proses)):
    print("\nwaktu : ",gT)
    iterator=0
    nomor=1
    nomor2=1
    nomor3=1
    for i in proses:
        
        if i[2] >= 0:
            if i[1] == 1:
                print('qA, FCFS antrian-',nomor)
                if i[0] not in antrianFCFS[tes]:
                    antrianFCFS.append([])
                    antrianFCFS[tes].append(i[0])
                    #antrianFCFS[tes].append(i[2])
                #if antrianFCFS[tes][1] == -1:
                if i[2] == -1:
                    del antrianFCFS[0]
                print("sisa waktu proses ",i[0]," : ",i[2])
                #print(tes," ",(antrianFCFS[tes]))
                if i[0] == antrianFCFS[tes][0]:
                    i[2]-=1
                    #antrianFCFS[tes][1]-=1
                    #i[2]=antrianFCFS[tes][1]
                if i[2] == -1:
                    done+=1
                    print("================== proses yang telah selesai : ",done)
                    tes+=1
                nomor+=1
                '''
                '''
            elif i[1]==2:
                print('qB, Round Robbin antrian-',nomor2)
                print("sisa waktu proses ",i[0]," : ",i[2])
                i[2]-=1
                if i[2] == -1:
                    done+=1
                    print("================== proses yang telah selesai : ",done)
                nomor2+=1

            elif i[1]==3:
                print('qC, non-preemptive SJF antrian-',nomor2)
                print("sisa waktu proses ",i[0]," : ",i[2])
                i[2]-=1
                if i[2] == -1:
                    done+=1
                    print("================== proses yang telah selesai : ",done)
                nomor3+=1
            print("\n")
    gT+=1
    input("tekan enter..")
        
        
    