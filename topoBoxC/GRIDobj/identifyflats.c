#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>
#include <string.h>

void identifyflats(int rows, int cols, float *input, float *flats, float *stills){
    // Check for flats
    for(int row = 0; row < rows; row++){
        for (int col = 0; col < cols; col++){
            int index = row*cols+col;
            int tmp = 0;

            for (int x = row-1; x <= row+1; x++){
                for (int y = col-1; y <= col+1; y++){
                    // index = x*cols+y
                    // Skip if out of bounds
                    if(x < 0 || x >= rows || y < 0 || y >= cols) continue; 
                    // Skip if current cell
                    if(x == row && y == col) continue; 

                    if(input[index] <= input[x*cols+y]) tmp ++;
                }
            }
            if(tmp == 8){
                flats[index] = 1;
            }
        }
    }
    // Check for stills
    for(int row = 0; row < rows; row++){
        for (int col = 0; col < cols; col++){
            int index = row*cols+col;

            // Skip if cell is flat 
            if(flats[index] == 1) continue;

            int tmp = 0;
            int check = 0;
            for (int x = row-1; x <= row+1; x++){
                if(flats[row*cols+col] == 1) break;
                for (int y = col-1; y <= col+1; y++){
                    int current = x*cols+y;

                    // Skip if out of bounds
                    if (x < 0 || x >= rows || y < 0 || y >= cols) continue; 
                    // Skip if current cell
                    if (x == row && y == col) continue; 
                    if(input[index] > input[current])tmp = 1 ;
                    if(flats[current] == 1) check = 1;
                    
                }
            }
            if (tmp = 1 && check == 1){
                stills[index] = 1;
            }
        }
    }
}