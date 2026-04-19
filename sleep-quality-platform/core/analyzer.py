
class SleepAnalyzer:
    def __init__(self, target, data):
        self.target = target
        self.records = data

    def total(self, r):
        return sum(r)

    def count_good(self):
        return sum(1 for r in self.records if self.total(r) >= self.target)

    def stats(self):
        totals = [self.total(r) for r in self.records]
        return min(totals), max(totals), sum(totals)//len(totals)

    def evaluate(self, r):
        t = self.total(r)
        wake, rem, deep, light = r

        score = 0
        if t >= self.target:
            score += 1
        if rem >= 0.2 * t:
            score += 1
        if deep >= 0.13 * t:
            score += 1
        if wake < 0.15 * t:
            score += 1

        labels = ["SCADENTE", "DISCRETA", "BUONA", "ECCELLENTE"]
        return labels[min(max(score - 1, 0), 3)]

    def evaluations(self):
        return [self.evaluate(r) for r in self.records]

    def top5(self):
        totals = sorted([self.total(r) for r in self.records], reverse=True)
        return sorted(totals[:5])
