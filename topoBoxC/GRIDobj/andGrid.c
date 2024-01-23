#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>
#include <string.h>

void gradient8(int rows, int cols, float *input1, float *input2, float *output)
{
    for(int i = 0; i < cols*rows; i++)
    {
        if(input1[i] == input2[i] && input1[i] == 1)
        {
            output[i] = 1;
        }
    }
}