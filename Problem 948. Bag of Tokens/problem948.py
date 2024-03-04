'''
You start with an initial power of power, an initial score of 0, and a bag of tokens given as an integer array tokens, where each tokens[i] donates the value of tokeni.

Your goal is to maximize the total score by strategically playing these tokens. In one move, you can play an unplayed token in one of the two ways (but not both for the same token):

Face-up: If your current power is at least tokens[i], you may play tokeni, losing tokens[i] power and gaining 1 score.
Face-down: If your current score is at least 1, you may play tokeni, gaining tokens[i] power and losing 1 score.
Return the maximum possible score you can achieve after playing any number of tokens.



Example 1:

Input: tokens = [100], power = 50

Output: 0

Explanation: Since your score is 0 initially, you cannot play the token face-down. You also cannot play it face-up since your power (50) is less than tokens[0] (100).

Example 2:

Input: tokens = [200,100], power = 150

Output: 1

Explanation: Play token1 (100) face-up, reducing your power to 50 and increasing your score to 1.

There is no need to play token0, since you cannot play it face-up to add to your score. The maximum score achievable is 1.

Example 3:

Input: tokens = [100,200,300,400], power = 200

Output: 2

Explanation: Play the tokens in this order to get a score of 2:

Play token0 (100) face-up, reducing power to 100 and increasing score to 1.
Play token3 (400) face-down, increasing power to 500 and reducing score to 0.
Play token1 (200) face-up, reducing power to 300 and increasing score to 1.
Play token2 (300) face-up, reducing power to 0 and increasing score to 2.
The maximum score achievable is 2.
'''
from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:

        def face_up(token, power, score):
            power -= token
            score += 1
            return power, score


        def face_down(token, power, score):
            power += token
            score -= 1
            return power, score

        tokens.sort()
        score = 0
        l_pointer = 0
        r_pointer = len(tokens) - 1
        scores = []

        while l_pointer <= r_pointer:
            if power >= tokens[l_pointer]:
                power, score = face_up(tokens[l_pointer], power, score)
                scores.append(score)
                l_pointer += 1
                #print(power, score)
            else:
                if score >= 1:
                    power, score = face_down(tokens[r_pointer], power, score)
                    r_pointer -= 1
                    scores.append(score)
                    #print(power, score, r_pointer)
                else:
                    break

        return max(scores) if scores else 0



solution = Solution()

tokens = [200,100]
power = 150

tokens = [100,200,300,400]
power = 200

print(solution.bagOfTokensScore(tokens, power))
