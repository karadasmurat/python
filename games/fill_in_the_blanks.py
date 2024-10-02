import random


s1 = "In a linear model, the goal is to predict the target value based on the input features."
kw1 = ["linear model", "target", "features"]

s2 = "A data scientist is a professional who uses their knowledge of statistics, computer science, and domain expertise to extract insights from data."
kw2 = ["data scientist", "statistics",
       "computer science", "domain expertise", "insights"]


class FIB:
    def __init__(self, sentence, keywords):
        self.sentence = sentence
        self.keywords = keywords
        random.shuffle(self.keywords)
        self.blanked = self.get_blanked()

    def get_blanked(self) -> str:
        blanked = self.sentence
        for kw in self.keywords:
            blanked = blanked.replace(kw, "_______")

        return blanked

    def __repr__(self) -> str:
        return f"FIB(sentence={self.sentence}, keywords={self.keywords})"


data1 = {"sentences": [s1, s2], "keywords": [kw1, kw2]}
data2 = {s1: kw1, s2: kw2}

qnum = 1
for k in data2:
    fib = FIB(k, data2[k])
    print(f"{qnum}. {fib.blanked}")
    print(fib.keywords)

    qnum += 1

# print(blanked)
# print(words1)
