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
            if (buffer[0] == 'L') {
                buffer[0] = '-';
            } else {
                buffer[0] = '+';
            }
            int distance = atoi(buffer);
            dial += distance;
            while (dial > 99) {
                dial -= 100;
            }
            while (dial < 0) {
                dial += 100;
            }
            if (dial == 0) {
                answer++;
            }
        }
        printf("answer = %d\n", answer);
        fclose(f);
    }
    return 0;
}
