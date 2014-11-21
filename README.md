Exercise 3
==========

This is the solution for exercise 3 of the
[Machine Learning Lecture][machine_learning] at the University of Bonn.

Contributors:
* Timm Behner
* Philipp Bruckschen
* Patrick Kaster
* Markus Schwalb

style file: [HMC Mathematics Homework Class]

[machine_learning]: http://www-kd.iai.uni-bonn.de/index.php?page=teaching_details&id=83
[HMC Mathematics Homework Class]: https://www.math.hmc.edu/computing/support/tex/classes/hmcpset/



Usage
----------------------

Usage: gradient_descent.py [options]

Options:
  -h, --help            show this help message and exit
  -e VALUE, --eta=VALUE
                        size of steps
  -m NUMBER, --maxiter=NUMBER
                        maximum number of iterations
  -t VALUE, --threshold=VALUE
                        threshold of errors

Termination Criterion
-----------------------

The gradient descent terminates after a fixed number on iterations which can be
set with the --maxiter option, or if the error is below a certain threshold
which can be set by --threshold. The default value for the maximum of iterations
is 100000. The default value for the threshold is 0.

Example
-----------------------

Example output with different values for eta:
eta_values = [0.5, 0.4, 0.3, 0.25, 0.2, 0.15, 0.1, 0.05, 0.01, 0.001]

ETA: 0.5
0.043289277561774364
0.01508320906411642
0.03355991819573201
[0, 0, 0] 0 0
[0, 0, 1] 0 0
[0, 1, 0] 0 0
[0, 1, 1] 0 0
[1, 0, 0] 0 0
[1, 0, 1] 1 0
[1, 1, 0] 1 0
[1, 1, 1] 1 0
Running time: 0.0006582736968994141 sec

ETA: 0.4
Terminated because error_count is lower threshold of 0
0.4850951822644578
0.07287606812465486
0.07103875488299771
[0, 0, 0] 0 0
[0, 0, 1] 0 0
[0, 1, 0] 0 0
[0, 1, 1] 0 0
[1, 0, 0] 0 0
[1, 0, 1] 1 1
[1, 1, 0] 1 1
[1, 1, 1] 1 1
Running time: 0.0008764266967773438 sec

ETA: 0.3
1.2217292132722655
0.659024481327925
0.6946039041195461
[0, 0, 0] 0 0
[0, 0, 1] 0 1
[0, 1, 0] 0 1
[0, 1, 1] 0 1
[1, 0, 0] 0 1
[1, 0, 1] 1 1
[1, 1, 0] 1 1
[1, 1, 1] 1 1
Running time: 0.0006189346313476562 sec

ETA: 0.25
1.0047313281504522
0.5268088075639146
0.5825472916317411
[0, 0, 0] 0 0
[0, 0, 1] 0 1
[0, 1, 0] 0 1
[0, 1, 1] 0 1
[1, 0, 0] 0 1
[1, 0, 1] 1 1
[1, 1, 0] 1 1
[1, 1, 1] 1 1
Running time: 0.00057220458984375 sec

ETA: 0.2
Terminated because error_count is lower threshold of 0
0.4383906476465432
0.24854423984173352
0.09299232258035878
[0, 0, 0] 0 0
[0, 0, 1] 0 0
[0, 1, 0] 0 0
[0, 1, 1] 0 0
[1, 0, 0] 0 0
[1, 0, 1] 1 1
[1, 1, 0] 1 1
[1, 1, 1] 1 1
Running time: 0.0005850791931152344 sec

ETA: 0.15
Terminated because error_count is lower threshold of 0
0.4701678242516529
0.21136576407718724
0.2465282279448204
[0, 0, 0] 0 0
[0, 0, 1] 0 0
[0, 1, 0] 0 0
[0, 1, 1] 0 0
[1, 0, 0] 0 0
[1, 0, 1] 1 1
[1, 1, 0] 1 1
[1, 1, 1] 1 1
Running time: 0.0007193088531494141 sec

ETA: 0.1
Terminated because error_count is lower threshold of 0
0.33281561888409555
0.1924910187983455
0.18018980057783404
[0, 0, 0] 0 0
[0, 0, 1] 0 0
[0, 1, 0] 0 0
[0, 1, 1] 0 0
[1, 0, 0] 0 0
[1, 0, 1] 1 1
[1, 1, 0] 1 1
[1, 1, 1] 1 1
Running time: 0.0010080337524414062 sec

ETA: 0.05
Terminated because error_count is lower threshold of 0
0.36354765346655854
0.24099964588846717
0.21700222418314696
[0, 0, 0] 0 0
[0, 0, 1] 0 0
[0, 1, 0] 0 0
[0, 1, 1] 0 0
[1, 0, 0] 0 0
[1, 0, 1] 1 1
[1, 1, 0] 1 1
[1, 1, 1] 1 1
Running time: 0.0010457038879394531 sec

ETA: 0.01
Terminated because error_count is lower threshold of 0
0.32817979985059964
0.19617818918817914
0.20017050182303675
[0, 0, 0] 0 0
[0, 0, 1] 0 0
[0, 1, 0] 0 0
[0, 1, 1] 0 0
[1, 0, 0] 0 0
[1, 0, 1] 1 1
[1, 1, 0] 1 1
[1, 1, 1] 1 1
Running time: 0.0007138252258300781 sec

ETA: 0.001
Terminated because error_count is lower threshold of 0
0.30238375528114675
0.19923722811536815
0.2260431604339795
[0, 0, 0] 0 0
[0, 0, 1] 0 0
[0, 1, 0] 0 0
[0, 1, 1] 0 0
[1, 0, 0] 0 0
[1, 0, 1] 1 1
[1, 1, 0] 1 1
[1, 1, 1] 1 1
Running time: 0.001032114028930664 sec
