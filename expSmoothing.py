print("SOLN:----------------------------------------------------------------------------------------------")
# input values
t = [1,2,3,4,5,6]
A = [4.3,6.3,5.4,4.1,7.6,6.2]
# predicted n quarter moving average
w = 0.4
F = []
diffA_F = []
diffA_Fsq = []
sum_t = sum_A = mean_t = mean_A = 0.0
for i in range(0,len(t)):
    sum_A = sum_A + A[i]
    sum_t = sum_t + t[i]
mean_A = sum_A / len(t)
mean_t = sum_t / len(t)
avgSum = 0.0
avg_round_sum = 0.0
F.append(mean_A)
for i in range(1,len(t)):
    avgSum = w * A[i-1] + (1 - w) * F[i-1]
    avg_round_sum = round(avgSum, 2)
    F.append(avg_round_sum) 
k = 0.0
for i in range(0,len(F)):
    k = A[i] - F[i]
    diffA_F.append(round(k,2))
    diffA_Fsq.append(round(k*k,2))
rmse = 0.0
sumdiffA_Fsq = 0.0
for i in range(len(F)):
    sumdiffA_Fsq = sumdiffA_Fsq + diffA_Fsq[i]
rmse = ( sumdiffA_Fsq / len(t) ) ** 0.5

print("T > ",end="        ")
print(t)
print("A  > ",end="       ")
print(A)
print("F  > ",end="       ")
print(F)
print("(A-F)  > ",end="   ")
print(diffA_F)
print("(A-F)^2  > ",end=" ")
print(diffA_Fsq)
print("Sum of sq of error > ",end=" ")
print(round(sumdiffA_Fsq, 2))
print("RMSE > ",end=" ")
print(round(rmse, 2))
print("Mean of A = %.2f" % round(mean_A, 2))
print("Mean of t = %.2f" % round(mean_t, 2))