
//#include<opencv2/imgcodecs.hpp>
//#include<opencv2/imgproc.hpp>
//#include<opencv2/highgui.hpp>
//using namespace cv;
//#include<iostream>
//using namespace std;
//
//int main() {
//	int f=0;
//	cv::Mat img;
//	cv::VideoCapture cap(0);
//	if (!cap.isOpened()) {
//		f = 1;
//	}
//	while (f=1) {//display 
//		cap.read(img);
//		//rectangle(img,Point(100,100),Point(300,300),Scalar(0,255,0),1);
//		
//		imshow("hi", img);
//			cv::waitKey(1);
//	}
//}
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
using namespace cv;
#include <iostream>


using namespace std;

/////////////// Color Detection //////////////////////

void main() {

	char r;
	Mat img;
	VideoCapture cap(0);
	Mat imgHSV, mask;
	int hmin = 0, smin = 110, vmin = 153;
	int hmax = 19, smax = 240, vmax = 255;

	

	namedWindow("Trackbars", (640, 200));
	createTrackbar("Hue Min", "Trackbars", &hmin, 179);
	createTrackbar("Hue Max", "Trackbars", &hmax, 179);
	createTrackbar("Sat Min", "Trackbars", &smin, 255);
	createTrackbar("Sat Max", "Trackbars", &smax, 255);
	createTrackbar("Val Min", "Trackbars", &vmin, 255);
	createTrackbar("Val Max", "Trackbars", &vmax, 255);

	while (true) {
		cap.read(img);
		cvtColor(img, imgHSV, COLOR_BGR2HSV);
		Scalar lower(hmin, smin, vmin);
		Scalar upper(hmax, smax, vmax);
		inRange(imgHSV, lower, upper, mask);

		imshow("Image", img);
		imshow("Image HSV", imgHSV);
		imshow("Image Mask", mask);
		
		
	}
}