#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(long long w, long long h) {
    long long answer = 1;
    long long gcd = 0;

    for(int i = (w<h)?w:h; i > 0; i--)
    {
        if(w % i == 0 && h % i == 0)
        {
            gcd = i;
            break;
        }
    }

    answer = (w*h) - (w + h - gcd);

    return answer;
}