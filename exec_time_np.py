# program executes 2 algorithms with different time efficiencies (linear
# and quadratic) and measures execution time as a function of input size.
import time
import random
import math

def main():
    list_sizes1 = [x for x in range(10000, 50001, 5000)]
    exec_times_linear = []
    exec_times_quadratic = []
    
    # run experiment to measure execution time as a function of 
    # input size.  
    for list_size in list_sizes1:
        # create list of random ints of size list_size
        numbers = random.sample(range(1,1000000), list_size)
        # start the clock
        start = time.time()
        # perform some operation on each list element
        for num in numbers:
            result = math.sqrt(num) * math.sqrt(num)
        # stop the clock
        end = time.time()
        # save the execution time
        exec_times_linear.append(end-start)
    
    print("\n\n\tLinear growth")
    print("Input size \tExecution time (s) ")
    for i in range(len(list_sizes1)):
         print("%d \t\t %.5f" % (list_sizes1[i], exec_times_linear[i]))
    
    # Repeat the same process but with nested loops and 2 lists
    # of size n
    list_sizes2 = [x for x in range(1000, 5001, 500)]
    for list_size in list_sizes2:
        numbers1 = random.sample(range(1,100000), list_size)
        numbers2 = random.sample(range(1,100000), list_size)
        
        start = time.time()
        # Nested loops each iterating n times yields n^2 operations.
        # Execution time grows quadratically as a result
        for num1 in numbers1:
            for num2 in numbers2:
                    result = num1 * num2
        end = time.time()
        # save execution time
        exec_times_quadratic.append(end-start)        
    
    print("\n\n\tQuadratic growth")
    print("Input size \tExecution time (s)")
    for i in range(len(list_sizes2)):
        print("%d \t\t %.5f" % (list_sizes2[i], exec_times_quadratic[i]))    

if __name__ == "__main__":
    main()
    