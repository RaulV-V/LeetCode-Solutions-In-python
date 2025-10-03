class Solution:
    def hIndex(self, citations: List[int]) -> int:
        cnt = Counter(citations)
        freq = sorted(cnt.items(), key=lambda kv: kv[0], reverse=True)

        total = 0       
        h = 0
        for cite, how_many in freq:
            total += how_many
            h = max(h, min(total, cite))
        return h