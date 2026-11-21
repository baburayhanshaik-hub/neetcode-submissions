
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        lets = set("".join(words))

        dic = {ch: set() for ch in lets}
        order = {ch: 0 for ch in lets}

        dq = deque()

        for i in range(1, n):
            mini = min(len(words[i]), len(words[i-1]))

            if words[i-1][:mini] == words[i][:mini]:
                if len(words[i-1]) > len(words[i]):
                    return ""

            for j in range(mini):
                if words[i-1][j] != words[i][j]:

                    prev = words[i-1][j]
                    curr = words[i][j]

                    if curr not in dic[prev]:
                        dic[prev].add(curr)
                        order[curr] += 1

                    break

        for ch in lets:
            if order[ch] == 0:
                dq.append(ch)

        result = []


        while dq:
            ch = dq.popleft()
            result.append(ch)

            for nei in dic[ch]:
                order[nei] -= 1

                if order[nei] == 0:
                    dq.append(nei)

        if len(result) != len(lets):
            return ""

        return "".join(result)