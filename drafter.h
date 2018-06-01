#include <string>
#include <map>
#include <iostream>
using namespace std;

struct playerinformation
{
public:
   int draftamount;
   int twokrating;
   string position;
};

extern map<string, playerinformation> nbamap;

