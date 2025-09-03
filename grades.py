def average_score(scores: list[int]) -> float:
    sum = 0
    for score in scores:
        sum += score
    return sum/len(scores)


def pass_fail(score: int) -> str:
    if (score >= 60):
        return "Pass"
    else:
        return "Fail"


def analyze_scores(scores: list[int]) -> None:
    for score in scores:
        print(f"Score {score} -> {pass_fail(score)}")
    return None


if __name__ == "__main__":
    scores = [95, 82, 67, 54, 100, 73]
    print("All scores:", scores)
    print("Class average:", average_score(scores))
    analyze_scores(scores)
