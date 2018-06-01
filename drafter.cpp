#include "drafter.h"
#include <iostream>
using namespace std;

std::map<std::string, playerinformation>nbamap;


int main(void){
  playerinformation first;
  first.twokrating = 50;
  first.position = "forward";
  first.draftamount = 60,000;
  nbamap["kent"] = first;
  for(map<string,playerinformation>::iterator it = nbamap.begin(); it!=nbamap.end();++it){
    std::cout << it->first << " => " << it->second.twokrating << '\n';
  }
  return 0;
}
