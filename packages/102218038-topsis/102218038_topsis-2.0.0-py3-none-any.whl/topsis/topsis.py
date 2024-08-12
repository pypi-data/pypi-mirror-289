import pandas as pd
import numpy as np
import math as m 
import numbers as num
import sys
def norm(a):
    sqsum = 0
    for i in range(len(a)):
        sqsum += a.iloc[i]**2
    a = a/m.sqrt(sqsum)
    return a
    
def normall(data):
    check = data.isna()
    for i in range(len(check)):
        row = check.iloc[i]
        for j in range(len(row)):
            if row.iloc[j] or not isinstance(data.iloc[i,j],num.Number):
                raise ValueError(f"error at place ({i},{j}) in input data, value either not numeric or missing ")
    temp = data.T
    for i in range(len(temp)):
        temp.iloc[i,:] = norm(temp.iloc[i,:])
    
    data = temp.T
    return data

def topsis(d,w1,inc1):
    d = normall(d)
    colnames = np.array(d.columns)
    w = w1.split(",")
    inc = inc1.split(",")
    wl = len(w)
    cal = d.T
    dl= len(cal)
    if  wl != dl:
        raise IndexError("un-even matrices passes, columns of data: {dl} and number of weights passed: {wl}")
    if len(inc) != dl:
        raise IndexError("un-even matrices passes, columns of data: {dl} and number of inclinations passed: {wl}")
    best = []
    worst = []
    for i in range(dl):
        cal.iloc[i,:] = cal.iloc[i,:]*float(w[i])
        if inc[i] == "+":
            best.append(max(cal.iloc[i,:]))
            worst.append(min(cal.iloc[i,:]))
        elif inc[i] == "-":
            best.append(min(cal.iloc[i,:]))
            worst.append(max(cal.iloc[i,:]))
        else:
            raise ValueError(f"""leave no separation between input impacts, example if acceptable imput: "+,-,+,-", example of wrong input: "+, - ,+ ,-" """)
    # print(cal.T)
    d = cal.T
    distp = []
    distn = []
    for i in range(len(d)):
        b = 0
        w0 = 0
        for j in range(dl):
            b += (d.iloc[i,j]-best[j])**2
            w0 += (d.iloc[i,j]-worst[j])**2
        distp.append(m.sqrt(b))
        distn.append(m.sqrt(w0))
    p = []
    # print("distn:",distn)
    # print("distp:",distp)
    for i in range(len(distn)):
        p.append(distn[i]/(distn[i]+distp[i]))
    ret = []
    # print(p)
    i = 0
    for row in range(len(d)):
        # print(row)
        # print("i: ",i)
        # print(d.iloc[row,:])
        ret.append([*np.array(d.iloc[row,:]),p[i]])
        i+=1
    colnames = np.append(colnames,"TOPSIS score")
    d = pd.DataFrame(ret,columns=colnames)
    
    return p

def run(inp_path, weights, impacts, outpath):
    print("converting your data!")
    
    data = pd.read_csv(inp_path)
    d = data.drop(data.columns[0],axis=1)
    
    pscore = topsis(d,weights,impacts)
    data["Topsis Score"] = pscore
    data['Rank'] = data['Topsis Score'].rank(method='max', ascending=False).astype(int)
    
    data.to_csv(outpath, index=False)
    print("RESULT FILE UPDATED")

# def main():
#     print("converting your data!")
    
#     data = pd.read_csv(sys.argv[0])
#     d = data.drop(data.columns[0],axis=1)
    
#     pscore = topsis(d,sys.argv[1],sys.argv[2])
#     data["Topsis Score"] = pscore
#     data['Rank'] = data['Topsis Score'].rank(method='max', ascending=False).astype(int)
    
#     output_file=sys.argv[4]
#     data.to_csv(output_file, index=False)
#     print("RESULT FILE UPDATED") 
    
# if __name__ =="__main__":
#     main()
# d = pd.DataFrame([[1,2,3,4],[2,3,4,5]])
# imp = "+,+,+,-,+"
# weight = "0.25,0.25,0.25,0.25,0.25"
# print(run("out.csv",weight,imp,"giveme.csv"))