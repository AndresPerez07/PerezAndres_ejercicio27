#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <math.h>

using namespace std;

float euler_explicit(int i, float dt,float t_ini, float t_fin, float omega);
float euler_implicit(int i, float dt,float t_ini, float t_fin, float omega);
void muere_explicit(int i, float dt,float t_ini, float t_fin, float omega);
void muere_implicit(int i, float dt,float t_ini, float t_fin, float omega);

int main() {

  float omega = 1.0;

  float t_ini = 0.0;
  float t_fin = 4.0/omega;
  float *dt = new float[3];

  dt[0]=0.1/omega;
  dt[1]=0.01/omega;
  dt[2]=1.0/omega;

  float sol_exp;
  float sol_imp;
  float error_exp;
  float error_imp;
  float sol_ana = exp(-omega*(4.0/omega));

  for (size_t i = 0; i < 3; i++) {
    sol_exp = euler_explicit(i, dt[i],t_ini, t_fin, omega);
    sol_imp = euler_implicit(i, dt[i],t_ini, t_fin, omega);
    error_exp = (sol_ana-sol_exp)/sol_ana;
    error_imp = (sol_ana-sol_imp)/sol_ana;
    cout << "Error fraccional con (omega*dt = " << dt[i] << ") = " << error_exp/error_imp << endl;
  }

  float dt_prueba = 0.0;

  for (size_t i = 0; i < 10; i++) {
    dt_prueba = dt_prueba + 0.1;
    muere_explicit(i, dt_prueba,t_ini, t_fin, omega);
    muere_implicit(i, dt_prueba,t_ini, t_fin, omega);
  }



  delete[]dt;

  return 0;
}
float euler_explicit(int i, float dt,float t_ini, float t_fin, float omega){

ofstream file;
file.open("euler_exp_" + to_string(i)+ ".txt");
float t = t_ini;
float y = 1.0;
file << t << " " << y << endl;
  while (t < t_fin) {

    y = y - dt*omega*y;
    t = t + dt;
    file << t << " " << y << endl;
  }

  file.close();
  return y;
}

float euler_implicit(int i,float dt,float t_ini, float t_fin, float omega){

ofstream file;
file.open("euler_imp_" + to_string(i)+ ".txt");
float t = t_ini;
float y = 1.0;
file << t << " " << y << endl;
  while (t < t_fin) {

    y = y/(1.0+ dt*omega);
    t = t + dt;
    file << t << " " << y << endl;
  }

  file.close();
  return y;
}

void muere_explicit(int i, float dt,float t_ini, float t_fin, float omega){

ofstream file;
file.open("muere_exp_" + to_string(i)+ ".txt");
float t = t_ini;
float y = 1.0;
file << t << " " << y << endl;
  while (t < t_fin) {

    y = y - dt*omega*y;
    t = t + dt;
    file << t << " " << y << endl;
  }

  file.close();
}
void muere_implicit(int i, float dt,float t_ini, float t_fin, float omega){

ofstream file;
file.open("muere_imp_" + to_string(i)+ ".txt");
float t = t_ini;
float y = 1.0;
file << t << " " << y << endl;
  while (t < t_fin) {

    y = y/(1.0+ dt*omega);
    t = t + dt;
    file << t << " " << y << endl;
  }

  file.close();
}
