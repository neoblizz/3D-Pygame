//
//  main.c
//  3d
//
//  Created by Yuxiang Chen on 2/23/15.
//  Copyright (c) 2015 Yuxiang Chen. All rights reserved.
//

#include <stdio.h>
#include "math.h"
#include "transform.c"
#define PI 3.14159265
const int n = 3;

int main ()
{
    int ret;
    
    /* calling a function to get max value */
    int dir = 1;
    float angle = PI / 8;
    printf("%f\n", angle);
    int vector[4] = {1,0,0,0};
    ret = rotation(dir,angle,vector);
    printf( "Max value is : %d\n", ret );
    
    return 0;
}


int rotation(dir, angle, vector)
{
    float a = cos (angle);
    float b = sin (angle);
    double x[4][4] = {{1,0,0,0},{0,1,0,0},{0,0,1,0},{0,0,0,1}};
    if (dir == 1){
        //x = {{1,0,0,0},{0,a,-1*b,0},{0,b,a,0},{0,0,0,1}};
        x[1][1] = a;
        x[1][2] = -1.0 * b;
        x[2][1] = b;
        x[2][2] = a;
        printf( "1\n");
    }else if (dir == 2){
        //x = {{a,0,b,0},{0,1,0,0},{-1*b,0,a,0},{0,0,0,1}};
        x[0][0] = a;
        x[0][2] = b;
        x[2][0] = -1.0 * b;
        x[2][2] = a;
        printf( "2\n");
    }else if (dir == 3){
        //x = {{a,-1*b,0,0},{b,a,0,0},{0,0,1,0},{0,0,0,1}};
        x[0][0] = a;
        x[0][1] = -1.0 * b;
        x[2][0] = b;
        x[2][2] = a;
        printf( "3\n");
    }
    
    print_a(4,4,x);
    return 0;
}

int translation(trans_x,trans_y,trans_z,vector)
{
    double x[4][4] = {{1,0,0,trans_x},{0,1,0,trans_y},{0,0,1,trans_z},{0,0,0,1}};
    print_a(4,4,x);
    return 0;
}

int scale(scale_x, scale_y, scale_z,vector)
{
    double x[4][4] = {{scale_x,0,0,0},{0,scale_y,0,0},{0,0,scale_z,0},{0,0,0,1}};
    print_a(4,4,x);
    return 0;
}

int matrixMulti()
{
    return 1;
}


int print_a(int m, int n, double arr[][n])
{
    int i, j;
    for (i = 0; i < m; i++){
        for (j = 0; j < n; j++){
            printf("%lf ", arr[i][j]);
        }
        printf("\n");
    }
    return 0;
}