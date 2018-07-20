#include <iostream>
#include "tools.h"

using Eigen::VectorXd;
using Eigen::MatrixXd;
using std::vector;

Tools::Tools() {}

Tools::~Tools() {}

VectorXd Tools::CalculateRMSE(const vector<VectorXd> &estimations,
                              const vector<VectorXd> &ground_truth) {
  /**
  TODO:
    * Calculate the RMSE here.
  */
	VectorXd rmse(4);
	rmse << 0, 0, 0, 0;

	if ((estimations.size() != ground_truth.size()) || estimations.size() == 0)
	{
		//Bcout << "Invalid estimation or ground_truth data" << endl;
		return rmse;
	}

	//accumulate squared residuals
	for (unsigned int i = 0; i < estimations.size(); ++i) {

		VectorXd residual = estimations[i] - ground_truth[i];
		//cout << "residual " << i << "value is " << residual << endl;
		//coefficient-wise multiplication
		residual = residual.array()*residual.array();
		//cout << "residual sq" << i << "value is " << residual << endl;
		rmse += residual;
		//cout << "rmse value is " << rmse << endl;
	}

	//calculate the mean
	rmse = rmse / estimations.size();

	//calculate the squared root
	rmse = rmse.array().sqrt();

	cout << "rmse = " << rmse << endl;
	return rmse;
}