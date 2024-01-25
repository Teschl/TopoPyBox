#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>
#include <string.h>

void identifyflats(int rows, int cols, float *input, float *flats, float *sills){
    // Check for flats
    for(int row = 0; row < rows; row++){
        for (int col = 0; col < cols; col++){
            int index = row*cols+col;
            int tmp = 0;

            for (int x = row-1; x <= row+1; x++){
                for (int y = col-1; y <= col+1; y++){
                    int neighbor = x*cols+y;

                    // Skip if out of bounds
                    if(x < 0 || x >= rows || y < 0 || y >= cols) continue; 
                    // Skip if current cell
                    if(x == row && y == col) continue; 
                    // if neighbor not lower
                    if(input[index] <= input[neighbor]) tmp ++;
                }
            }
            // if all neigbors are not lower
            if(tmp == 8){
                flats[index] = 1;
            }
        }
    }
    // Check for stills
    for(int row = 0; row < rows; row++){
        for (int col = 0; col < cols; col++){
            int index = row*cols+col;

            // skip if flat at index
            if(flats[index] == 1) continue;

            for (int x = row-1; x <= row+1; x++){
                for (int y = col-1; y <= col+1; y++){
                    int neighbor = x*cols+y;

                    // Skip if out of bounds
                    if (x < 0 || x >= rows || y < 0 || y >= cols) continue; 
                    // Skip if current cell
                    if (x == row && y == col) continue;

                    // --------------------
                    if(flats[neighbor] == 1){
                        sills[index] = 1;
                    }
                    // --------------------
                }
            }
        }
    }
}