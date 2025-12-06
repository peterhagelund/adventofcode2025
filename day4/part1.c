#include <math.h>
#include <memory.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int DELTAS[8][2] = {
    {-1, -1},
    {-1, 0},
    {-1, 1},
    {0, -1},
    {0, 1},
    {1, -1},
    {1, 0},
    {1, 1},
};

int main(int argc, char *argv[]) {
    FILE *f = fopen("puzzle_input.txt", "rt");
    if (f == NULL) {
        return EXIT_FAILURE;
    }
    int height = 0;
    int width = 0;
    char **floor = malloc(256 * sizeof(char *));
    char buffer[256];
    while (fgets(buffer, sizeof(buffer), f) != NULL) {
        size_t len = strlen(buffer);
        if (len > 1) {
            len--;
            buffer[len] = '\0';
        }
        if (len > width) {
            width = len;
        }
        floor[height] = malloc(256);
        strcpy(floor[height], buffer);
        height++;
    }
    int answer = 0;
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            if (floor[y][x] != '@') {
                continue;
            }
            int count = 0;
            for (int i = 0; i < 8; i++) {
                int _y = y + DELTAS[i][0];
                int _x = x + DELTAS[i][1];
                if ((_y >= 0) && (_y < height) && (_x >= 0) && (_x < width) && (floor[_y][_x] == '@')) {
                    count++;
                }
            }
            if (count < 4) {
                answer++;
            }
        }
    }
    for (int y = 0; y < height; y++) {
        free(floor[y]);
        floor[y] = NULL;
    }
    free(floor);
    fclose(f);
    printf("answer = %d\n", answer);
    return EXIT_SUCCESS;
}