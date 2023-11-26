inputMatrix = [
    2, 3, 5, 7, 8;
    2, 1, 4, 6, 9;
    3, 4, 6, 7, 10;
    5, 6, 8, 9, 11;
    5, 6, 7, 8, 10];
    
outputMatrix = mex_aspect(inputMatrix);
disp('Input Matrix:');
disp(inputMatrix);
disp('Output Matrix:');
disp(outputMatrix);
%imshow(outputMatrix);