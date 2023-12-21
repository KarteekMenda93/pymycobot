%MATLAB code

clear all clc

syms a1 a2 a3 a4 a5 t1 t2 t3 t4 t5 t6 the1 the2 the3 the4 the5 the6
a1= 131.56; a2 = 110.4; a3 =96; a4 =73.18; a5 = 66.39 ; a6 = 43.6;

% theta1 = 0,theta2 = 90,theta3 =-60, theta4 = 0,theta5 = 0, theta6 = 20
tt1=0/180*pi; 

tt2=90/180*pi; 

tt3=-60/180*pi; 

tt4=0/180*pi;

tt5=0/180*pi; 

tt6=20/180*pi; 




% Forward
H01 = [cos(t1)  0   -sin(t1) 0;...
       sin(t1)  0    cos(t1) 0;...
       0        1    0       a1;...
       0        0    0       1]

H12= [cos(t2) -sin(t2)  0   a2*cos(t2);...
      sin(t2)  cos(t2)  0   a2*sin(t2);...
      0        0       -1   0;...
      0        0        0   1]

H23= [-cos(t3)   sin(t3)   0    a3*cos(t3);...
       sin(t3)  -cos(t3)   0    a3*sin(t3);...
       0         0        -1    0;...
       0         0         0    1]

H34= [-sin(t4)   0    cos(t4)    0;...
       cos(t4)   0    sin(t4)    0;...
       0        -1    0          a5;...
       0         0    0          1]

H45= [-sin(t5)   0    cos(t5)    0;...
       cos(t5)   0    sin(t5)    0;...
       0        -1    0          a4;...
       0         0    0          1]


H56= [cos(t6)   sin(t5)   0    0;...
      sin(t6)  -cos(t6)   0    0;...
      0         0         1    a6;...
      0         0         0    1]

H06 = simplify(H01*H12*H23*H34*H45*H56)

Px= (3231*sin(t1))/50 - (552*cos(t1)*sin(t2))/5 - (218*sin(t1)*sin(t5))/5 + (218*cos(t2 + t3 + t4)*cos(t1)*cos(t5))/5 - (3659*cos(t2 + t3)*cos(t1)*sin(t4))/50 - (3659*sin(t2 + t3)*cos(t1)*cos(t4))/50 - 96*cos(t1)*cos(t2)*sin(t3) - 96*cos(t1)*cos(t3)*sin(t2)
Py= (218*cos(t1)*sin(t5))/5 - (3231*cos(t1))/50 - (552*sin(t1)*sin(t2))/5 - 96*cos(t2)*sin(t1)*sin(t3) - 96*cos(t3)*sin(t1)*sin(t2) + (218*cos(t2 + t3 + t4)*cos(t5)*sin(t1))/5 - (3659*cos(t2 + t3)*sin(t1)*sin(t4))/50 - (3659*sin(t2 + t3)*cos(t4)*sin(t1))/50
Pz= 96*cos(t2 + t3) + (552*cos(t2))/5 - (3659*sin(t2 + t3)*sin(t4))/50 + cos(t5)*((218*cos(t2 + t3)*sin(t4))/5 + (218*sin(t2 + t3)*cos(t4))/5) + (3659*cos(t2 + t3)*cos(t4))/50 + 3289/25


 
px_new=vpa(subs(Px,[t1,t2,t3,t4,t5,t6],[tt1,tt2,tt3,tt4,tt5,tt6]))
py_new=vpa(subs(Py,[t1,t2,t3,t4,t5,t6],[tt1,tt2,tt3,tt4,tt5,tt6]))
pz_new=vpa(subs(Pz,[t1,t2,t3,t4,t5,t6],[tt1,tt2,tt3,tt4,tt5,tt6]))


% Given the joint angles, the e.e position is 
% px_new = -157.231292394998
% py_new = -64.62
% pz_new = 299.8741778