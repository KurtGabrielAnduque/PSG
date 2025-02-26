'''
A company has $1,000,000 to invest in different projects.
Each project has an associated cost and an expected return on investment (ROI).
The company wants to maximize its total return while staying within the budget.
'''



class Object:
    def __init__(self,P,C,R):
        self.projects = P
        self.Cost = C
        self.Returns = R


    def getCost(self):
        return self.Cost

    def getReturns(self):
        return self.Returns


    def getROI(self):
        return self.getReturns()/self.getCost()


    def __str__(self):
        return self.projects + "< " + str(self.Cost) + " , "+ str(self.Returns) + " >"



def BuildObject(P,C,R):
    Full_Object = []
    for x in range(len(R)):
        Full_Object.append(Object(P[x],C[x],R[x]))

    return Full_Object


def greedy_algorithm(Object,constraint,keyFunction):
    Object_Copy = sorted(Object, key = keyFunction)
    result = []

    total_cost = 0
    total_return = 0

    for i in range(len(Object)):
        if (total_cost + Object_Copy[i].getCost()) <= constraint:
            result.append(Object_Copy[i])
            total_cost += Object_Copy[i].getCost()
            total_return += Object_Copy[i].getReturns()

    return (result,total_cost)

def test_greedy(Objects,constraint,keyFunction):
    result, total_cost = greedy_algorithm(Objects,constraint,keyFunction)
    print(f'Total return using greed algorithm: {total_cost}')
    print(f'Projects taken:')
    for x in result:
        print(' ', x)


def testingGreedy(build,constraint):
    print(f'testing greedy algorithm with constraint: {constraint} get best ROI')
    print('\n')
    test_greedy(build,constraint, Object.getROI)






projects = ['Project A', 'Project B', 'Project C', 'Project D']
Cost = [250000, 100000, 500000, 200000]
Returns = [400000, 180000, 700000, 320000]
constraint = 1000000

build_object = BuildObject(projects,Cost,Returns)


testingGreedy(build_object,constraint)


