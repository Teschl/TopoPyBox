#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>

void aspect(int rows, int cols, float *input, float *output) {
    for(int i = 0; i<rows*cols; i++){
        output[i] = input[i];
    }
}