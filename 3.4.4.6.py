exam_mark=float(input("What is the exam mark?\n"))
print("The exam mark of %s corresponds to following grade:" %exam_mark)
if exam_mark<40:
    print("F3")
elif exam_mark>=40 and exam_mark<45:
    print("F2")
elif exam_mark>=45 and exam_mark<50:
    print("F1 Supp")
elif exam_mark>=50 and exam_mark<60:
    print("Third")
elif exam_mark>=60 and exam_mark<70:
    print("Second")
elif exam_mark>=70 and exam_mark<75:
    print("Upper Second")
elif exam_mark>=75:
    print("First")
