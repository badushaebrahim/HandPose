#include<opencv2/imgcodecs.hpp>
#include<opencv2/highgui.hpp>
#include<opencv2/imgproc.hpp>
#include<opencv2/opencv_modules.hpp>
#include<opencv2/opencv.hpp>
#include<vector>
#include<iostream>
#include<process.h>

//void getContour(cv::Mat ims,cv::Mat imres) {
//	vector<vector<Point>>contours;
//	findContours(ims, contours, hierarchy, cv::RetrievalModes::RETR_EXTERNAL, cv::ContourApproximationModes::CHAIN_APPROX_SIMPLE);
//
//
//}

int main() {
	//int x;
	cv::VideoCapture cap(0);
	cv::Mat img,imgCanny, imgDilate, imgGrey, imgBlur,imgtre,imgtesd;
	int low1 = 108,low2 = 23,low3 = 82;
	int hi1=179, hi2=255, hi3=255;
	
	while (true)
	{
		cap.read(img);
		
		cv::cvtColor(img,imgGrey,cv::COLOR_BGR2GRAY);
		//GaussianBlur(imgGrey, imgBlur,Size(3,3), 3,0 );
		Canny(img, imgCanny, 25,75);
		cv::Mat kernel = cv::getStructuringElement(cv::MORPH_RECT, cv::Size(2,2));
		dilate(imgCanny, imgDilate, kernel);
		imshow("og", img); imshow("gray", imgGrey); //imshow("blur", imgBlur); 
		imshow("canny", imgCanny);
		imshow("fg",imgDilate);
		cvtColor(img, imgtesd, cv::ColorConversionCodes::COLOR_BGR2HSV);
		
		cv::inRange(imgGrey, cv::Scalar(low1,low2,low3), cv::Scalar(hi1,hi2,hi3), imgtre);
		//cv::inRange(imgtesd, low22[1], hi22[1], imgtre);
		imshow("tesh", imgtesd);
		imshow("t2", imgtre);
		if(cv::waitKey(30) == 27) {
			std::cout << "exit";
			exit(1);
		 }
		 //std::cout << x<<"\n";
	}
}