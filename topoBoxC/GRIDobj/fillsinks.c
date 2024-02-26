#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>
#include <string.h>
#include <stdbool.h>

void fillsinks(int rows, int cols, float *input_matrix, float *output_matrix){
    bool changes = true;

    // fill sinks until there are no more sinks to fill
    while(changes){
        changes = false;

        // a cell is part of a sink, as long as all
        // neighbours are higher or part of a sink

        // start at 1 and end -1 so edges are not sinks
        for(int row = 1; row < rows-1; row++){
            for(int col = 1; col < cols-1; col++){
                int index = row * cols + col;
                bool sink = true;
                // some value to begin with
                float lowest_neighbour = input_matrix[index+1];

                for (int y = row-1; y <= row+1; y++){
                    for (int x = col-1; x <= col+1; x++){
                        int neighbor = y * cols + x;

                        // continue if out of bounds
                        if(x < 0 || x >= cols || y < 0 || y >= rows) continue; 
                        if(neighbor == index) continue;

                        //
                        if(input_matrix[index] >= input_matrix[neighbor]){
                            sink = false;
                            break;
                        }
                        if(input_matrix[neighbor] < lowest_neighbour) lowest_neighbour = input_matrix[neighbor];
                    }
                    if(!sink) break;
                }
                // 
                if(sink){
                    changes = true;
                    input_matrix[index] = lowest_neighbour;
                }
            }
        }
    }
}