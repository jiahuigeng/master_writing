import sys
if len(sys.argv)!=2:
    print("Usage: python get_best.py")
    exit(2)

filename = sys.argv[1]
with open(filename) as f:
    best_value = 0
    for line in f:
        if "Starting LM training epoch 1" in line:
            break
        if "csls_knn_10 - Precision at k = 1:" in line:
            best_value = max(best_value, float(line.split()[-1])) 
            #best_value = float(line.split()[-1])
        if "Writing translation results" in line:
            print(best_value)
print(best_value)