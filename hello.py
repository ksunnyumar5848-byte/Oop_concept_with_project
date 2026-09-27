class Students:

    def __init__(self,s_name,s_rollno,s_class):
        self.name=s_name
        self.roll=s_rollno
        self.standard=s_class

        print(f"{self.name} with roll no {self.roll} has enrolled ")

    def work(self):
        print(f"{self.name} working on their homeworkks ......")

rahul=Students("rahul Kesari ",5,10)

rahul.name="sunny "        