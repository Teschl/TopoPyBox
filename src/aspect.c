#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>
#include "aspect.h"

/*
rows = 3, cols = 3 with
0 1 2
3 4 5
6 7 8
index 0 = 0*3+0
index 5 = 1*3+2
index 6 = 2*3+0
*/

void aspect(int rows, int cols, float *input, float *output) {
    // check all cells
    for (int row = 0; row < rows; row++) {
        for (int col = 0; col < cols; col++) {

            int index = row*cols+col;

            float minVal = input[index];
            int result = 5; // default value is cell itself
            int count = 0;  // counter of neigbour cells

            // Check all 8 neighbors
            for (int i = row-1; i <= row+1; i++) {
                for (int j = col-1; j <= col+1; j++) {
                    count++;
                    // Skip if current cell
                    if (i == row && j == col) continue;
                    // Skip if out of bounds
                    if (i < 0 || i >= rows || j < 0 || j >= cols) continue;
                    // Check if smaller
                    if (input[i*cols+j] < minVal) {
                        minVal = input[i*cols+j];
                        result = count;
                    }
                }
            }
            // Assign output cell value
            output[index] = result;
        }
    }
}