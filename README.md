Lane Detection using image processing. Sobelx filter is used to detect vertical edges instead of general canny edge detection. Then normal Hough transform is used to detect lines passing through minimum 200 points. Then clutering of lines is removed by taking average of negative rho lines and ploting single lines. Similarly average is taken for positive rho.

#command to run the code
python3 lane-detection.py 

![Alt text](houghlines3.jpg raw=true "Houghline")