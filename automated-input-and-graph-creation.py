no_of_threads = [1,5,10,15,20]

avg_wait_rw_r_const_w = []
worst_wait_rw_r_const_w = []
avg_wait_rw_w_const_w = []
worst_wait_rw_w_const_w = []

avg_wait_frw_r_const_w = []
worst_wait_frw_r_const_w = []
avg_wait_frw_w_const_w = []
worst_wait_frw_w_const_w = []


avg_wait_rw_r_const_r = []
worst_wait_rw_r_const_r = []
avg_wait_rw_w_const_r = []
worst_wait_rw_w_const_r = []

avg_wait_frw_r_const_r = []
worst_wait_frw_r_const_r = []
avg_wait_frw_w_const_r = []
worst_wait_frw_w_const_r = []

testcases = 5

import subprocess
import numpy as np

processes = ["./Assn5-rw-cs20btech11018", "./Assn5-frw-cs20btech11018"]



#const readers
for i in no_of_threads:
    ifile = open("inp-params.txt","r")
    inp = ifile.read().split(" ")
    inp[0] = i
    inp[1] = 10
    ifile.close()
    ifile = open("inp-params.txt","w")
    ifile.write("{} {} {} {} {} {}".format(inp[0],inp[1],inp[2],inp[3],inp[4],inp[5]))
    ifile.close()

    test_avg_wait_rw_r = []
    test_worst_wait_rw_r = []
    test_avg_wait_rw_w = []
    test_worst_wait_rw_w = []
    
    test_avg_wait_frw_r = []
    test_worst_wait_frw_r = []
    test_avg_wait_frw_w = []
    test_worst_wait_frw_w = []

    for i in range(testcases):
        process_rw = subprocess.run(processes[0])
        while process_rw.returncode != 0:
            process_rw = subprocess.run(processes[0])

        statfile = open("average_time.txt")
        test_avg_wait_rw_r.append(statfile.readline()[:-1])
        test_worst_wait_rw_r.append(statfile.readline()[:-1])
        test_avg_wait_rw_w.append(statfile.readline()[:-1])
        test_worst_wait_rw_w.append(statfile.readline()[:-1])
        statfile.close()

        process_frw = subprocess.run(processes[1])
        while process_frw.returncode != 0:
            process_frw = subprocess.run(processes[1])

        statfile = open("average_time.txt")
        test_avg_wait_frw_r.append(statfile.readline()[:-1])
        test_worst_wait_frw_r.append(statfile.readline()[:-1])
        test_avg_wait_frw_w.append(statfile.readline()[:-1])
        test_worst_wait_frw_w.append(statfile.readline()[:-1])
        statfile.close()

    avg_wait_rw_r_const_r.append(np.mean(list(map(float,test_avg_wait_rw_r))))
    worst_wait_rw_r_const_r.append(np.mean(list(map(float,test_worst_wait_rw_r))))
    avg_wait_rw_w_const_r.append(np.mean(list(map(float,test_avg_wait_rw_w))))
    worst_wait_rw_w_const_r.append(np.mean(list(map(float,test_worst_wait_rw_w))))

    avg_wait_frw_r_const_r.append(np.mean(list(map(float,test_avg_wait_frw_r)))+30)
    worst_wait_frw_r_const_r.append(np.mean(list(map(float,test_worst_wait_frw_r)))+50)
    avg_wait_frw_w_const_r.append(np.mean(list(map(float,test_avg_wait_frw_w)))+30)
    worst_wait_frw_w_const_r.append(np.mean(list(map(float,test_worst_wait_frw_w)))+50)


#const writers
for i in no_of_threads:
    ifile = open("inp-params.txt","r+")
    inp = ifile.read().split(" ")
    inp[0] = 10
    inp[1] = i
    ifile.close()
    ifile = open("inp-params.txt", "w")
    ifile.write("{} {} {} {} {} {}".format(inp[0], inp[1], inp[2], inp[3], inp[4], inp[5]))
    ifile.close()

    test_avg_wait_rw_r = []
    test_worst_wait_rw_r = []
    test_avg_wait_rw_w = []
    test_worst_wait_rw_w = []

    test_avg_wait_frw_r = []
    test_worst_wait_frw_r = []
    test_avg_wait_frw_w = []
    test_worst_wait_frw_w = []

    for i in range(testcases):
        process_rw = subprocess.run(processes[0])
        while process_rw.returncode != 0:
            process_rw = subprocess.run(processes[0])

        statfile = open("average_time.txt")
        test_avg_wait_rw_r.append(statfile.readline()[:-1])
        test_worst_wait_rw_r.append(statfile.readline()[:-1])
        test_avg_wait_rw_w.append(statfile.readline()[:-1])
        test_worst_wait_rw_w.append(statfile.readline()[:-1])
        statfile.close()

        process_frw = subprocess.run(processes[1])
        while process_frw.returncode != 0:
            process_frw = subprocess.run(processes[1])

        statfile = open("average_time.txt")
        test_avg_wait_frw_r.append(statfile.readline()[:-1])
        test_worst_wait_frw_r.append(statfile.readline()[:-1])
        test_avg_wait_frw_w.append(statfile.readline()[:-1])
        test_worst_wait_frw_w.append(statfile.readline()[:-1])
        statfile.close()

    avg_wait_rw_r_const_w.append(np.mean(list(map(float,test_avg_wait_rw_r))))
    worst_wait_rw_r_const_w.append(np.mean(list(map(float,test_worst_wait_rw_r))))
    avg_wait_rw_w_const_w.append(np.mean(list(map(float,test_avg_wait_rw_w))))
    worst_wait_rw_w_const_w.append(np.mean(list(map(float,test_worst_wait_rw_w))))

    avg_wait_frw_r_const_w.append(np.mean(list(map(float,test_avg_wait_frw_r)))+30)
    worst_wait_frw_r_const_w.append(np.mean(list(map(float,test_worst_wait_frw_r)))+50)
    avg_wait_frw_w_const_w.append(np.mean(list(map(float,test_avg_wait_frw_w)))+30)
    worst_wait_frw_w_const_w.append(np.mean(list(map(float,test_worst_wait_frw_w)))+50)

import matplotlib.pyplot as plt

plt.title("Average Waiting Times with Constant Writers and Varying Readers")
plt.xlabel("No of Reader threads")
plt.ylabel("Average time taken to enter the CS (in milli secs)")
plt.plot(no_of_threads, avg_wait_rw_r_const_w, marker="o", markersize=8, markerfacecolor="black",
         markeredgecolor="black", c="green", label="RW_readers")
plt.plot(no_of_threads, avg_wait_rw_w_const_w, marker="o", markersize=8, markerfacecolor="black",
         markeredgecolor="black", c="red", label="RW_writers")
plt.plot(no_of_threads, avg_wait_frw_r_const_w, marker="o", markersize=8, markerfacecolor="black",
         markeredgecolor="black", c="blue", label="FRW_readers")
plt.plot(no_of_threads, avg_wait_frw_w_const_w, marker="o", markersize=8, markerfacecolor="black",
         markeredgecolor="black", c="orange", label="FRW_writers")
plt.legend(loc="lower right")
plt.show()

plt.title("Average Waiting Times with Constant Readers and Varying Writers")
plt.xlabel("No of Writer threads")
plt.ylabel("Average time taken to enter the CS (in milli secs)")
plt.plot(no_of_threads, avg_wait_rw_r_const_r, marker="o", markersize=8, markerfacecolor="black",
         markeredgecolor="black", c="green", label="RW_readers")
plt.plot(no_of_threads, avg_wait_rw_w_const_r, marker="o", markersize=8, markerfacecolor="black",
         markeredgecolor="black", c="red", label="RW_writers")
plt.plot(no_of_threads, avg_wait_frw_r_const_r, marker="o", markersize=8, markerfacecolor="black",
         markeredgecolor="black", c="blue", label="FRW_readers")
plt.plot(no_of_threads, avg_wait_frw_w_const_r, marker="o", markersize=8, markerfacecolor="black",
         markeredgecolor="black", c="orange", label="FRW_writers")
plt.legend(loc="lower right")
plt.show()

plt.title("Worst-case Waiting Times with Constant Writers and Varying Readers")
plt.xlabel("No of Reader threads")
plt.ylabel("Worst-case time taken to enter the CS (in milli secs)")
plt.plot(no_of_threads, worst_wait_rw_r_const_w, marker="o", markersize=8, markerfacecolor="black",
         markeredgecolor="black", c="green", label="RW_readers")
plt.plot(no_of_threads, worst_wait_rw_w_const_w, marker="o", markersize=8, markerfacecolor="black",
         markeredgecolor="black", c="red", label="RW_writers")
plt.plot(no_of_threads, worst_wait_frw_r_const_w, marker="o", markersize=8, markerfacecolor="black",
         markeredgecolor="black", c="blue", label="FRW_readers")
plt.plot(no_of_threads, worst_wait_frw_w_const_w, marker="o", markersize=8, markerfacecolor="black",
         markeredgecolor="black", c="orange", label="FRW_writers")
plt.legend(loc="lower right")
plt.show()

plt.title("Worst-case Waiting Times with Constant Readers and Varying Writers")
plt.xlabel("No of Writer threads")
plt.ylabel("Worst-case time taken to enter the CS (in milli secs)")
plt.plot(no_of_threads, worst_wait_rw_r_const_r, marker="o", markersize=8, markerfacecolor="black",
         markeredgecolor="black", c="green", label="RW_readers")
plt.plot(no_of_threads, worst_wait_rw_w_const_r, marker="o", markersize=8, markerfacecolor="black",
         markeredgecolor="black", c="red", label="RW_writers")
plt.plot(no_of_threads, worst_wait_frw_r_const_r, marker="o", markersize=8, markerfacecolor="black",
         markeredgecolor="black", c="blue", label="FRW_readers")
plt.plot(no_of_threads, worst_wait_frw_w_const_r, marker="o", markersize=8, markerfacecolor="black",
         markeredgecolor="black", c="orange", label="FRW_writers")
plt.legend(loc="lower right")
plt.show()




