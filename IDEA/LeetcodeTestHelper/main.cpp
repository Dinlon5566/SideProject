#include <iostream>
#include <string>
using namespace std;

int main(int argc,char** argv)
{
    string str(argv[1]);
    system(("ping "+str).c_str());
    return 0;
}
