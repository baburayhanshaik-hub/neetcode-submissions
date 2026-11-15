
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # Step 1: Sort tickets by destination
        tickets.sort(key=lambda x: x[1], reverse=True)

        # Step 2: Build adjacency list
        dic = {}

        for src, dst in tickets:
            if src not in dic:
                dic[src] = []

            dic[src].append(dst)

        # Step 3: Store the final itinerary
        res = []

        # Step 4: DFS function
        def dfs(node):

            # Keep exploring while outgoing flights exist
            while dic.get(node):

                # Take the lexicographically smallest destination
                nxt = dic[node].pop()

                dfs(nxt)

            # Add airport after all outgoing flights are used
            res.append(node)

        # Step 5: Start DFS from JFK
        dfs("JFK")

        # Step 6: Reverse the result
        return res[::-1]
