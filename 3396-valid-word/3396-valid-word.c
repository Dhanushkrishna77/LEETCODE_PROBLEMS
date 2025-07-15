bool isValid(char* word) {
    int len = strlen(word);
    if (len < 3) return false;
    
    bool hasVowel = false, hasConsonant = false;
    
    for (int i = 0; i < len; i++) {
        char c = tolower(word[i]);
        
        if (!isalnum(word[i])) return false;
        
        if (isalpha(word[i])) {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                hasVowel = true;
            } else {
                hasConsonant = true;
            }
        }
    }
    
    return hasVowel && hasConsonant;
}