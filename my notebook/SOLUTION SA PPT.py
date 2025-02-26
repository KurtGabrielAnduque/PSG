


''' 
You are about to sit down for a meal. You know how much you value different foods.But you have a calorie budget of not more than 800 calories.

'''



def DP_KNAPSACK(c,Cal,Val,n, FOOD):

    table = [[0 for x in range(c + 1)] for y in range(n + 1)]


    for item in range(n + 1):
        for calorie in range(c + 1):
            if item == 0 or calorie == 0:
                table[item][calorie] = 0

            elif Cal[item - 1] <= calorie:
                table[item][calorie] = max(
                    Val[item - 1] + table[item -1 ][calorie - Cal[item - 1]],
                    table[item - 1][calorie]
                )

            else:
                table[item][calorie] = table[item - 1][calorie]




    selected_item = []
    remaining_capacity = c

    for search in range(n, 0 , -1):
        if table[search][remaining_capacity] != table[search -1][remaining_capacity]:
            selected_item.append(FOOD[search - 1])
            remaining_capacity -= Cal[search - 1]


    return table[n][c],selected_item

constraint = 800
FOOD =['wine','beer','Pizza','Burger','Fries','coke','Apple','Donut']
Value = [89,90,30,50,90,79,90,10]
Calories = [123,154,258,354,365,150,95,195]
n = len(Value)


Max, items  = DP_KNAPSACK(constraint,Calories,Value,n,FOOD)

print(f'max value: {Max}')
print(f'Food eaten:')
for item in items:
    print(item)
