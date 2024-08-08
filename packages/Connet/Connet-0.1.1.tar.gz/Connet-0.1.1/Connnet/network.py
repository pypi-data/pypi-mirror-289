# Connnet/Connnet/network.py

def generate_network_file(network_file, LIs, filter_seq):
    with open(network_file, 'a+') as f:
        h = 0
        while h < len(filter_seq):
            y = filter_seq[h] 
            kl1 = LIs.index(y)
            thg = []
            for et in LIs:
                if et[0] == y[0] and et[1] == y[1] and et[2] == y[2] and et[3] == y[3] and et[4] == y[4] and et[5] == y[5] and et[6] == y[6] and et[7] == y[7]:
                    loc = LIs.index(et)
                    thg.append(loc) 
            
            LIs_use = [LIs[df] for df in range(0, len(LIs), 1) if df not in thg]  
            print(f'running, please wait')
            
            i = 0
            aList = []
            while i < 8:  
                for k in LIs_use:
                    if k[i] == y[i] and abs(k[8] - y[8]) < 1:  
                        aList.append(k) 
                i += 1 
            
            temp = []
            for dd in aList:  
                if dd not in temp:  
                    temp.append(dd)
            
            for z in temp:
                f.write(f'{y}|{z}')
                f.write("\n")
            
            h += 1
