


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name: str, age:int, tracks:list, score:float):
        self.name: str = name
        self.age: int = age
        self.tracks: list = tracks
        self.score: float = score
    def change_name(self,name):
        self.name=name
        return str [self.name]
    def change_age(self,age):
        self.age=age 
        return int[self.age]
    def add_track(self, tracks):
        self.tracks.append(tracks)
        return list[tracks]
    def get_score(self):
        return self.score
        



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
print (Bob.name,"is aged",Bob.age, ". He offers the following tracks",Bob.tracks,"and his totalscore is",Bob.score )
# Expected methods

Bob.change_name=("Peter")
Bob.change_age=(34)
Bob.add_track=(Bob.tracks,"UI/UX")
Bob.get_score=(Bob.score)
print(Bob.change_name,"is aged",Bob.change_age, ". He offers the following tracks",Bob.add_track,"and his totalscore is",Bob.get_score)
