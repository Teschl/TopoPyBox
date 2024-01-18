#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>


void aspect(int rows, int cols, float *input, float *output)
{
    // check all cells
    for (int row = 0; row < rows; row++) 
    {
        for (int col = 0; col < cols; col++) 
        {

            int index = row*cols+col;

            float minVal = input[index];
            int result = 5; // default value is cell itself
            int count = 0;  // counter of neighbour cells

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