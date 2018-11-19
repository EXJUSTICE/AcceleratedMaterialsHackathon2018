This is a submission for the problem statement provided by the NUSAMDWorkshop 2018 hackathon challenge.
I call this the "Quick n Dirty"

Details can be found here
https://github.com/acceleratedmaterials/Hackathon/blob/master/README.md

Support Vector Regression, Bayesian Ridge Regression, and 3D Linear Regression were used. SGD Regression was included, 
but tuning was not not optimized. Learning rate and scaling were identified as crucial for SGD Regression to avoid nonsensical results.

The current results are as follows (units were not specified, assuming A)

SVR 0.185 <br />
Bayesian 0.120 <br />
LR 0.121 <br />
SGDR 0.165 <br />

To run this code, make sure you have SKlearn, pandas, and numpy installed in spyder.


