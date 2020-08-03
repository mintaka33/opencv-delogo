#include "opencv2/core.hpp"
#include "opencv2/imgcodecs.hpp"
#include <opencv2/photo.hpp>
#include <iostream>

using namespace cv;

int main()
{
    Mat src = imread("1.jpg", IMREAD_COLOR);
    Mat dst = src;
    Mat mask = Mat::zeros(src.rows, src.cols, CV_8UC1);
    Rect logo_rect(1602, 80, 303, 117);
    mask(logo_rect) = Scalar(255);

    inpaint(src, mask, dst, 3, INPAINT_TELEA);
    imwrite("out.jpg", dst);
    return 0;
}