#from tkinter import*
#root=Tk()

#root.title("list")
#root.geometry("500x500")
#root.configure(bg="#EC9200")

subjects=("english","socialscience","science","Artificial Inteligence","Hindi","Maths","sanskrit")
marks=(74,75,78,80,79,68,70)

max_marks=max(marks)
print("the max marks are :"+str(max_marks))

maxSubjectIndex=marks.index(max_marks)
max_subject=subjects[maxSubjectIndex]
print("the subject name is: "+str(max_subject))

minimum_marks=min(marks)
minimum_subject_index=marks.index(minimum_marks)
minimum_subject=subjects[minimum_subject_index]
print("the minnimum marks are: "+str(minimum_marks)+" the subject name is: "+str(minimum_subject))


#root.mainloop()
