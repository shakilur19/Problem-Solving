class Solution:
    def permute(self, nums):
        result = []

        def dfs(path, remaining):
            if not remaining:
                result.append(path)
                return

            length = len(remaining)

            for i in range(length):
                new_path = path + [remaining[i]]
                new_remaining = remaining[:i] + remaining[i+1:]

                dfs(new_path, new_remaining)

        dfs([], nums)
        return result