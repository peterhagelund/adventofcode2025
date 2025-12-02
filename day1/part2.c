#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    FILE *f = fopen("puzzle_input.txt", "rt");
    if (f != NULL) {
        int answer = 0;
        int dial = 50;
        char buffer[80];
        while (fgets(buffer, sizeof(buffer), f) != NULL) {
            size_t len = strlen(buffer);
            buffer[len - 1] = '\0';
            int distance = atoi(buffer + 1);
            for (int i = 0; i < distance; i++) {
                if (buffer[0] == 'L') {
                    dial--;
                } else {
                    dial++;
                }
                if (dial == -1) {
                    dial = 99;
                } else if (dial == 100) {
                    dial = 0;
                }
                if (dial == 0) {
                    answer++;
                }
            }
        }
        printf("answer = %d\n", answer);
        fclose(f);
    }
    return 0;
}
