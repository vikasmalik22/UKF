# UKF -Unscented Kalman Filters in C++
Udacity CarND Term 2, Project 2 - Unscented Kalman Filters

## Project Basics
The main goal of the project is to apply Unscented Kalman Filter to fuse data from Lidar and Radar sensors of a self driving car using C++. The code will make a prediction based on the sensor measurement and then update the expected position.

See the starter code from Udacity Project 
[Starter Code](https://github.com/udacity/CarND-Unscented-Kalman-Filter-Project)

## Basic Build Instructions
1. Clone this repo.
2. Make a build directory: mkdir build && cd build
3. Compile: cmake .. && make
	On windows, you may need to run: cmake .. -G "Unix Makefiles" && make
4. Run it: ./UnscentedKF

## Contents of Repository
- src dir
	1. main.cpp - communicates with the Term 2 Simulator receiving data measurements, calls a function to run the Kalman filter, calls a function to calculate RMSE
	2. ukf.cpp -  initializes the Unscented Kalman filter, calls the predict and update function, defines the predict and update functions.
	4. tools.cpp- function to calculate RMSE and the Jacobian matrix
- data - a directory with one input file, provided by Udacity
- results - a directory with output and log files
- Docs - a directory with files formats description

## Project Model & Approach
In this project, I used a "constant turn rate and velocity magnitude" (CTRV) process model to carry out the Kalman filter's predict steps. The CTRV tracks a state vector of 5 quantities: x position, y position, velocity magnitude, yaw angle, and yaw rate. To predict the position from the time of the old measurement to the time of the current measurement, the velocity magnitude and yaw rate are assumed to be constant; however, a random linear (in the direction of the velocity) acceleration and yaw acceleration are assumed to exist at each time interval. Both accelerations are uncorrelated with a mean of zero and a constant variance.

Part of this project was choosing the hardcoded variance of the random linear and yaw rate accelerations applied during the predict step. The chosen values should be physically reasonable (i.e., a bike or car will not abruptly accelerate at 100 m/s^2, so the variance should be significantly less than 100^2). A good way to check if the noise values are physically reasonable is to use the "normalized information squared" or NIS statistic. If our chosen variances used in the prediction step are consistent with physical reality, the NIS values computed from the radar measurements should roughly obey a chi-square distribution with degrees of freedom equal to the dimension of the radar measurement space (3). A concrete heuristic way to check this is to plot the NIS statistic for the radar or lidar measurements along with the corresponding 95% confidence threshold of the chi-square distribution, which is 7.82 for 3 degrees of freedom (radar) and 5.991 for 2 degrees of freedom (lidar). If our noise is consistent, we should see roughly 95% of NIS values computed from measurements fall below that confidence threshold, which appears just about right for my chosen process noise variances (4 m^s/s^4 for the linear acceleration and 0.5 rad^2/s^4 for the yaw rate acceleration):

## Results
Using one set of simulated run (dataset 1), Unscented Kalman Filter produces the below results. The x-position is shown as 'px', y-position as 'py', velocity in the x-direction is 'vx', while velocity in the y-direction is 'vy'.

The graphs are created below using **ukf-visualization.ipynb** provided by [Mercedes Sensor Fusion Utilities](https://github.com/udacity/CarND-Mercedes-SF-Utilities)
This is done by logging the data in an output.txt file when running the prject with simulator.
Format of the logged data is prsenet in following sequence: ['px_est','py_est','vx_est','vy_est','px_meas','py_meas','px_gt','py_gt','vx_gt','vy_gt'].
This is then observed using **ukf-visualization.ipynb**.

NIS Values are observed using NIS.py file.

Threshold RMSE <= [.09, .10, .40, .30].

### 1. Laser-Radar Combined 
Set following compiler switches to:

ONLY_LASER 0
_ _ _

ONLY_RADAR 0

#### 1. Dataset 1
![Laser-Radar-Output-Dataset1](https://github.com/vikasmalik22/UKF/blob/master/results/ukf_combined_output.png)

Accuracy - RMSE [0.0727, 0.0819, 0.3019, 0.2810]
![Accuracy - RMSE](https://github.com/vikasmalik22/UKF/blob/master/results/rmse_combined_dataset1.PNG)

[ukf_output1.txt](https://github.com/vikasmalik22/UKF/blob/master/results/combined_output.txt)

[NIS Radar](https://github.com/vikasmalik22/UKF/blob/master/results/Radar_NIS_combined.png)

[NIS Lidar](https://github.com/vikasmalik22/UKF/blob/master/results/Laser_NIS_combined.png)

### 2. Lidar Only

Set following compiler switches to:

ONLY_LASER 1
_ _ _

ONLY_RADAR 0

![Lidar-Output-Dataset1](https://github.com/vikasmalik22/UKF/blob/master/results/ukf_lidar_output.png)

Accuracy - RMSE [0.102878, 0.09486, 0.5474, 0.2910]

[ukf lidar_output1.txt](https://github.com/vikasmalik22/UKF/blob/master/results/laser_only_output.txt)

[UKF NIS Lidar Only](https://github.com/vikasmalik22/UKF/blob/master/results/Laser_NIS_only.png)

### 3. Radar Only

Set following compiler switches to:

ONLY_LASER 0
_ _ _

ONLY_RADAR 1

#### 1. Dataset 1
![Radar-Output-Dataset1](https://github.com/vikasmalik22/UKF/blob/master/results/ukf_radar_output.png)

Accuracy - RMSE [0.1643, 0.2625, 0.4091, 0.3546]

[ukf radar_output1.txt](https://github.com/vikasmalik22/UKF/blob/master/results/radar_only_output.txt)

[UKF NIS Radar Only](https://github.com/vikasmalik22/UKF/blob/master/results/Radar_NIS_only.png)


## Observation
From the above results (RMSE values), Lidar data seems to provide more accurate positining readings (px, py) than Radar. Whereas, Radar provides a bit more accurate velocity readings than Lidar. Combining both of them strengthens the UKF algorithm to predict the position & velocity more precisely.