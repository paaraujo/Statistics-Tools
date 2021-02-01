import numpy as np

with open("sample1.txt", "w") as f:
    for i in range(3):
        f.write(str(np.random.normal(0.1,0.02))+"\n")
f.close()

with open("sample2.txt", "w") as f:
    for i in range(20):
        f.write(str(np.random.normal(0.1,0.02))+"\n")
f.close()

with open("sample3.txt", "w") as f:
    for i in range(100):
        f.write(str(np.random.normal(0.1,0.02))+"\n")
f.close()

with open("sample4.txt", "w") as f:
    for i in range(500):
        f.write(str(np.random.normal(0.1,0.02))+"\n")
f.close()

with open("sample5.txt", "w") as f:
    for i in range(1000):
        f.write(str(np.random.normal(0.1,0.02))+"\n")
f.close()

with open("sample6.txt", "w") as f:
    for i in range(2000):
        f.write(str(np.random.normal(0.1,0.02))+"\n")
f.close()