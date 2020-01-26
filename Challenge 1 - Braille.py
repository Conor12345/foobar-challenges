def solution(s):
    letterDict = {}

    nums = "000001" \
           "011110" \
           "110010" \
           "100010" \
           "000000" \
           "111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"

    words = "The quick brown fox jumps over the lazy dog"

    newWords = ""
    for letter in words:
        if letter.isupper():
            newWords += "0"
            newWords += letter.lower()
        else:
            newWords += letter.lower()


    for i in range(0, int(len(nums)), 6):
        letterDict[newWords[int(i / 6)]] = nums[i:i + 6]

    outStr = ""
    for letter in s:
        if letter.isupper():
            outStr += letterDict["0"]
        outStr += letterDict[letter.lower()]

    return outStr