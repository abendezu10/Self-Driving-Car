#include <iostream>
#include "opencv2/opencv.hpp"

using namespace cv;
using namespace std;

int main () {
 
  VideoCapture cap(0);

  waitKey(1000);

  Mat save_img; cap >> save_img;

  if(save_img.empty())
  {
    cerr << "Image was not captured!";

  }
  
  imwrite("pictures/test.jpg", save_img);
  cout<<"Hello World!";
  


  return 0;
}
