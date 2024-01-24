#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>
#include <string.h>

#define M_PI 3.14159265358979323846

void gradient8(int rows, int cols, float *input, float *output, int unit, float distance)
{
    for(int row = 0; row < rows; row++){
        for (int col = 0; col < cols; col++){
            
            int index = row*cols+col;
            float steepest = 0;
            float diagonal = sqrt(2*distance*distance);

            for (int x = row-1; x <= row+1; x++){
                for (int y = col-1; y <= col+1; y++){

                    int neighbor = x*cols+y;
                    float diff = abs(input[index]-input[neighbor]);

                    // Skip if out of bounds
                    if(x < 0 || x >= rows || y < 0 || y >= cols) continue; 
                    // Skip if current cell
                    if(neighbor == index) continue;
                    // if neighbor is corner 
                    if(x != row && y != col){
                        if(diff/diagonal > steepest){
                            steepest = diff/diagonal;
                        }
                    }else{
                        if(diff/distance > steepest){
                            steepest = diff/distance;
                        }
                    }
                }
            }
            switch (unit)
                    {
                    case 0:
                        output[index] = steepest;
                        break;
                    case 1:
                        output[index] = atan(steepest);
                        break;
                    case 2:
                        output[index] = atan(steepest)*(180/M_PI);
                        break;
                    case 3: 
                        output[index] = sin(atan(steepest));
                        break;
                    case 4:
                        output[index] = steepest*100;
                        break;
                    default:
                        break;
                    }
        }
    }
}