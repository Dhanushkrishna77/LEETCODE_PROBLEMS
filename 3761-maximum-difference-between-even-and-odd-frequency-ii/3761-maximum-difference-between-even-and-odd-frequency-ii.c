static int maxDifference(const char *s, int k) {
    int n = (int)strlen(s);
    if (n < k) return -1;
    unsigned char *arr = malloc(n);
    if (!arr) return -1;
    int total[5] = {0,0,0,0,0};
    for (int i = 0; i < n; i++) {
        unsigned char d = (unsigned char)(s[i] - '0');
        arr[i] = d;
        if (d < 5) total[d]++;
    }
    int ans = INT_MIN;
    for (int da = 0; da < 5; da++) {
        int tA = total[da];
        if (tA < 1) continue;
        int maxOddA = (tA & 1) ? tA : (tA - 1);
        if (maxOddA < 1) continue;
        for (int db = 0; db < 5; db++) {
            if (db == da) continue;
            int tB = total[db];
            if (tB < 2) continue;
            int possible = maxOddA - 2;
            if (possible <= ans) continue;
            int bestMin[4] = { INT_MAX, INT_MAX, INT_MAX, INT_MAX };
            int cntA = 0, cntB = 0, preA = 0, preB = 0, left = -1;
            for (int right = 0; right < n; right++) {
                unsigned char v = arr[right];
                cntA += (v == da);
                cntB += (v == db);
                while (right - left >= k && (cntB - preB) >= 2) {
                    int st = ((preA & 1) << 1) | (preB & 1);
                    int diff = preA - preB;
                    if (diff < bestMin[st]) bestMin[st] = diff;
                    left++;
                    unsigned char vl = arr[left];
                    preA += (vl == da);
                    preB += (vl == db);
                }
                int statusR = ((cntA & 1) << 1) | (cntB & 1);
                int target = statusR ^ 2;
                int bm = bestMin[target];
                if (bm != INT_MAX) {
                    int cur = cntA - cntB - bm;
                    if (cur > ans) ans = cur;
                }
            }
        }
    }
    free(arr);
    return (ans == INT_MIN ? -1 : ans);
}


int bacon(char *s, int k) {
    return maxDifference(s, k); //b4c0λ
}