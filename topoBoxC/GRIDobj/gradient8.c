#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>
#include <string.h>

#define M_PI 3.14159265358979323846

void gradient8(int rows, int cols, float *input, float *output, int unit, float distance)
{
    // rows = wie breit ist eine col (und anders herum)
    for(int col = 0; col < cols; col++)
    {
        for(int row = 0; row < rows; row++)
        {
            int index = col*rows + row;
            float min_cell_value = input[index];

            // assign indexis to all neighbour cells
            int left = index-1;
            int right = index+1;
            int top_left = index-cols-1;
            int top = index-cols;
            int top_right = index-cols+1;
            int bot_left = index+cols-1; 
            int bot = index+cols; 
            int bot_right = index+cols+1;

            // make sure index is never out of range
            if (col == 0) { 
                left = index;
                top_left = index;
                bot_left = index; 
            }
            if (col == cols - 1) { 
                right = index;
                top_right = index;
                bot_right = index; 
            }
            if (row == 0) { 
                top = index;
                top_left = index;
                top_right = index; 
            }
            if (row == rows - 1) { 
                bot = index;
                bot_left = index;
                bot_right = index; 
            }

            // compare min cell value to all neighbour cells
            input[top_left] < min_cell_value ? min_cell_value = input[top_left],
            output[index] = abs(input[index] - min_cell_value) / sqrt(pow(distance,2)) : 0;

            input[top]      < min_cell_value ? min_cell_value = input[top],
            output[index] = abs(input[index] - min_cell_value) / distance  : 0;

            input[top_right]< min_cell_value ? min_cell_value = input[top_right],
            output[index] = abs(input[index] - min_cell_value) / sqrt(pow(distance,2))  : 0;

            input[left]     < min_cell_value ? min_cell_value = input[left],
            output[index] = abs(input[index] - min_cell_value) / distance  : 0;

            input[right]    < min_cell_value ? min_cell_value = input[right],
            output[index] = abs(input[index] - min_cell_value) / distance  : 0;

            input[bot_left] < min_cell_value ? min_cell_value = input[bot_left],
            output[index] = abs(input[index] - min_cell_value) / sqrt(pow(distance,2))  : 0; 

            input[bot]      < min_cell_value ? min_cell_value = input[bot],
            output[index] = abs(input[index] - min_cell_value) / distance  : 0;

            input[bot_right]< min_cell_value ? min_cell_value = input[bot_right],
            output[index] = abs(input[index] - min_cell_value) / sqrt(pow(distance,2))  : 0;
        }
    }

    // "tan": 0 (default), "rad": 1, "deg": 2, "sin": 3, "per": 4 

    switch (unit){
    case 1:
        for (int i = 0; i < rows*cols; i++){
            output[i] = atan(output[i]);
        }
        
    case 2:
        for (int i = 0; i < rows*cols; i++){
            output[i] = atan(output[i])*(180/M_PI);
        }
    case 3:
        for (int i = 0; i < rows*cols; i++){
            output[i] = sin(atan(output[i]));
        }
    case 4:
        for (int i = 0; i < rows*cols; i++){
            output[i] = output[i]*100;
        }
    default:
        break;
    }
}