def fun_with_anagrams(text):
    word_set = set()
    result = []

    for word in text:
        if ''.join(sorted(word)) not in word_set:
            result.append(word)
            word_set.add(''.join(sorted(word)))
            
    return(sorted(result))
    


def main():
    anagrams = ["code", "doce", "ecod", "frame", "framer", "ramef", "angle", "angel", "lange"]
    result = fun_with_anagrams(anagrams)
    print(result)

    anagrams = ["doce", "code", "ecod", "ramef", "frame", "framer", "lange", "angle", "angel"]
    result = fun_with_anagrams(anagrams)
    print(result)

if __name__ == "__main__":
    main()