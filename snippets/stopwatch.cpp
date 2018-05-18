#include <iostream>
#include <time.h>
#include <sys/timeb.h>
using namespace std;



class StopWatch {
public:
    int starts;
    int startm;
    struct timeb timebuffer;
    StopWatch () {
        ftime(&this->timebuffer);
        this->starts = this->timebuffer.time;
        this->startm = this->timebuffer.millitm;
    }
    
    inline int get_milli_time () {
        ftime(&this->timebuffer);
        return (this->timebuffer.time - this->starts) * 1000 + (this->timebuffer.millitm - this->startm);
    }
};
int main () {
    StopWatch sw;
    
    
    cout << sw.get_milli_time() << endl;
    
    return 0;
}