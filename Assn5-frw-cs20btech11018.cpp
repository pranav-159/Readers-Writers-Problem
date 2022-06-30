#include <iostream>
#include <fstream>
#include <thread>
#include <chrono>
#include <semaphore>
#include <random>
#include <functional>
#define ll long long

using namespace std;
using std::cout;
using std::endl;
using std::chrono::duration_cast;
using std::chrono::microseconds;
using std::chrono::milliseconds;
using std::chrono::seconds;
using std::chrono::system_clock;

int kw, kr;
float tCS, tR;

int readcount=0;
std::binary_semaphore rmutex{1};
std::binary_semaphore resource{1};
std::binary_semaphore serviceQueue{1};


std::binary_semaphore out_mutex{1};

std::default_random_engine generator;
// output file
std::ofstream logfile("FRW_log.txt");
std::fstream avgfile("average_time.txt", ios::out);

ll wait_sum_r = 0;
ll wait_sum_w = 0;
ll worst_wait_r = 0;
ll worst_wait_w = 0;

inline ll time_since_epoch()
{
    return duration_cast<microseconds>(system_clock::now().time_since_epoch()).count();
}

std::string sysTime(ll microseconds)
{
    time_t t = microseconds / 1000000;
    std::string str = ctime(&t);
    while (str == "")
    {
        t = (long long)time_since_epoch() / 1000000;
        str = ctime(&t);
    }
    return str.substr(11, 8) + "." + to_string(microseconds % 1000000);
}

void writer(int);
void reader(int);

int main(int argc, char const *argv[])
{
    logfile << "Log_FRW:\n";
    std::ifstream ifile("inp-params.txt");

    int nw, nr, kw_i, kr_i;
    float tCS_i, tR_i;

    ifile >> nw >> nr >> kw_i >> kr_i >> tCS_i >> tR_i;

    // global variable setting
    kw = kw_i;
    kr = kr_i;
    tCS = tCS_i;
    tR = tR_i;

    std::thread writers[nw];
    std::thread readers[nr];

    // writers and readers initialization
    for (int i = 0; i < nw; i++)
    {
        writers[i] = std::thread(std::bind(writer, i + 1));
    }
    for (int i = 0; i < nr; i++)
    {
        readers[i] = std::thread(std::bind(reader, i + 1));
    }

    // writers and readers join
    for (int i = 0; i < nw; i++)
    {
        writers[i].join();
    }
    for (int i = 0; i < nr; i++)
    {
        readers[i].join();
    }
    std::fstream avgfile("FRW_average_time.txt", ios::out);
    avgfile << "Average waiting time for readers: " << (double)wait_sum_r / (nr * kr) << "\n";
    avgfile << "Average waiting time for writers: " << (double)wait_sum_w / (nw * kw) << "\n";
    avgfile.close();

    logfile.close();

    return 0;
}

void writer(int id)
{

    std::exponential_distribution<double> distribution_critical(1000 / tCS);
    std::exponential_distribution<double> distribution_remainder(1000 / tR);

    for (int i = 0; i < kw; i++)
    {
        std::string suffix;
        switch (i + 1)
        {
        case 1:
            suffix = "st ";
            break;
        case 2:
            suffix = "nd ";
            break;
        case 3:
            suffix = "rd ";
            break;
        default:
            suffix = "th ";
        }

        ll req_micro = time_since_epoch();
        std::string reqTime = sysTime(req_micro);
        out_mutex.acquire();
        logfile << i + 1 << suffix << "CS Request by Writer Thread " << id
                << " at " << reqTime << "\n";
        out_mutex.release();

        // entry synchronisation code
        serviceQueue.acquire();
        resource.acquire();
        serviceQueue.release();

        ll enter_micro = time_since_epoch();
        std::string enterTime = sysTime(enter_micro);
        out_mutex.acquire();
        logfile << i + 1 << suffix << "CS Entry by Writer Thread " << id
                << " at " << enterTime << "\n";
        int wait_milli = (enter_micro - req_micro)/1000;
        wait_sum_w += wait_milli;
        if(wait_milli > worst_wait_w)
            worst_wait_w = wait_milli;
        out_mutex.release();

        // critical section
        std::chrono::duration<double> sleep_CS(distribution_critical(generator));
        std::this_thread::sleep_for(sleep_CS);

        // exit synchronisation code
        resource.release();

        ll exit_micro = time_since_epoch();
        std::string exitTime = sysTime(exit_micro);
        out_mutex.acquire();
        logfile << i + 1 << suffix << "CS Exit by Writer Thread " << id
                << " at " << exitTime << "\n";
        out_mutex.release();

        // remainder section
        std::chrono::duration<double> sleep_R(distribution_remainder(generator));
        std::this_thread::sleep_for(sleep_R);
    }
}
void reader(int id)
{

    std::exponential_distribution<double> distribution_critical(1000 / tCS);
    std::exponential_distribution<double> distribution_remainder(1000 / tR);

    for (int i = 0; i < kr; i++)
    {
        std::string suffix;
        switch (i + 1)
        {
        case 1:
            suffix = "st ";
            break;
        case 2:
            suffix = "nd ";
            break;
        case 3:
            suffix = "rd ";
            break;
        default:
            suffix = "th ";
        }
        ll req_micro = time_since_epoch();
        std::string reqTime = sysTime(req_micro);
        out_mutex.acquire();
        logfile << i + 1 << suffix << "CS Request by Reader Thread " << id
                << " at " << reqTime << "\n";
        out_mutex.release();

        // entry synchronisation code
        serviceQueue.acquire();
        rmutex.acquire();
        readcount++;
        if(readcount == 1)
            resource.release();
        serviceQueue.release();
        rmutex.release();

        ll enter_micro = time_since_epoch();
        std::string enterTime = sysTime(enter_micro);
        out_mutex.acquire();
        logfile << i + 1 << suffix << "CS Entry by Reader Thread " << id
                << " at " << enterTime << "\n";
        int wait_milli = (enter_micro - req_micro) / 1000;
        wait_sum_r += wait_milli;
        if (wait_milli > worst_wait_r)
            worst_wait_r = wait_milli;
        out_mutex.release();

        // critical section
        std::chrono::duration<double> sleep_CS(distribution_critical(generator));
        std::this_thread::sleep_for(sleep_CS);

        // exit synchronisation code
        rmutex.acquire();
        readcount--;
        if (readcount == 0)
            resource.release();
        rmutex.release();

        ll exit_micro = time_since_epoch();
        std::string exitTime = sysTime(exit_micro);
        out_mutex.acquire();
        logfile << i + 1 << suffix << "CS Exit by Reader Thread " << id
                << " at " << exitTime << "\n";
        out_mutex.release();

        // remainder section
        std::chrono::duration<double> sleep_R(distribution_remainder(generator));
        std::this_thread::sleep_for(sleep_R);
    }
}
