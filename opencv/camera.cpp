#include <iostream>
#include <cstdlib>
#include <chrono>
#include <thread>
#include <csignal>


#include "opencv2/opencv.hpp"

using namespace cv;
using namespace std;

bool running = true;

void signalHandler(int signum) {
    cout << "\nInterrupt signal (" << signum << ") received. Exiting..." << endl;
    running = false;
}

int main () 
{
  signal(SIGINT, signalHandler);


  int img_count = 0; 
  
  string fname;

  VideoCapture cap(0);

  waitKey(1000);

  Mat save_img; 

 

  while(running){

    
    fname = "pictures/image" + to_string(img_count) + ".jpg";
    
     if(img_count == 10){

      int result = system("./.scripts/perase.sh");
      cout<<"Script ran!"<<endl;

    }


    cap >> save_img;
    imwrite(fname, save_img);
    img_count++; 
    
    this_thread::sleep_for(chrono::seconds(2));
    

  }

  int result = system("./.scripts/perase.sh"); 


  return 0;
}
