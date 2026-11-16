def word_break(s, word_dict):
    word_set = set(word_dict)
    memory = {}

    def check(remaining):
        if remaining == "":
            return True

        if remaining in memory:
            return memory[remaining]

        for i in range(1, len(remaining) + 1):
            prefix = remaining[:i]
        
            if prefix in word_set:
                if check(remaining[i:]):
                    memory[remaining] = True
                    return True
            
        memory[remaining] = False
        return False
    return check(s)

print(word_break("leetcode", ["leet", "code"]))
print(word_break("applepenapple", ["apple", "pen"]))
print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))
