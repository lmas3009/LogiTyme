**_Resulted Output while running in CLoud Provider:_**

```text

Performance Analysis

1. Introduction:
	This report presents the findings of a performance analysis conducted on the Python program 'testing-cloud.py'. The purpose of the analysis is to provide insights into the time consumed by the program and offer recommendations for optimizing its performance.

2. Methodolgy:
	The program was profiled using the cProfile module to collect data on execution time. The collected data was analyzed to identify the functions consuming the most time.

3. Results:
	- Started the program at: 2024-07-23 11:36:31.370432
	- Ended the program at: 2024-07-23 11:36:31.378430
	- Total Execution Time: 0.007 seconds
	- As you defined the threshold limit as 5 mins, Since this script took Less then your threshold limit, you are good to go...
	- memory consumed: 0.0039MB

4. Functions Results:
+----------------+---------------+-----------------------------+
| Function Name  | Time Consumed | Maximum Threshold Limit Set |
+----------------+---------------+-----------------------------+
| slow_function  | 0.003 secs    | 180 secs                    |
| slow_function2 | 0.003 secs    | 300 secs                    |
+----------------+---------------+-----------------------------+

5. inBuilt-functions Time-Consumed Report:
+----------------------------------+---------------+
| Function Name                    | Time Consumed |
+----------------------------------+---------------+
| <built-in method builtins.print> | 0.007 secs    |
+----------------------------------+---------------+

6. Environment Suggestions:
	- Short tasks (less than 5 minutes):
		-- GCP (Cloud Functions, Compute Engine, GKE, Cloud Run) or AWS (Lambda, EC2, ECS, Step Function, Glue): 
			 Both are well-suited for tasks that complete quickly.
		-- Azure Functions (Consumption Plan, VM, AKS, Container Instances):
			 Good choice for short tasks

7. Code Optimization:
+----------------+---------------+-----------------------------+
| Function Name  | Time Consumed | Maximum Threshold Limit Set |
+----------------+---------------+-----------------------------+
| slow_function  | 0.003 secs    | 180 secs                    |
| slow_function2 | 0.003 secs    | 300 secs                    |
+----------------+---------------+-----------------------------+
Since this function "slow_function" took 0.003 secs is less then 180 seconds (i.e < 3 mins). The function is quite optimized. 
Since this function "slow_function2" took 0.003 secs is less then 300 seconds (i.e < 5 mins). The function is quite optimized. 

8. Conclusion:
	The analysis revealed areas for potential optimization in the Python program 'testing-cloud.py'. By implementing the recommendations outlined in this report, the program's performance can be improved, leading to better overall efficency.

```