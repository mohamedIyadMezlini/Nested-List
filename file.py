if __name__ == '__main__':
    students=[]
    scores=[]
    Minimum=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student=[]
        student.append(name)
        student.append(score)
        scores.append(score)
        students.append(student)
    scores=sorted(set(scores))
    Snd_minimum=scores[1]
    for element ,key in students:
        if key == Snd_minimum:
            Minimum.append(element)
    Minimum=sorted(Minimum)
    for i in Minimum:
        print(i)