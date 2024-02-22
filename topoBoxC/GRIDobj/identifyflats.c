#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>
#include <string.h>

void identifyflats(int rows, int cols, float *inputMatrix, float *flatsMatrix, float *sillsMatrix){
    // rows: how many rows
    // cols: how many cols
    // inputMatrix: pointer to start of input matrix, size = rows * cols
    // flatsMatrix: pointer to start of flats matrix, size = rows * cols
    // sillsMatrix: pointer to start of sills matrix, size = rows * cols

    // loop through all cells on the input matrix:
    for(int row = 0; row < cols; row++){
        for(int col = 0; col < rows; col++){
            int index = row * cols + col;

            // loop through all 8 neighbours
            for (int x = row-1; x <= row+1; x++){
                for (int y = col-1; y <= col+1; y++){


                }
            }
        }
    }
}