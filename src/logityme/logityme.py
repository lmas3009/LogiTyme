"""
LogiTyme:
    LogiTyme is a Python package used to track the time spent on each function,
    custom functions, and the entire Python Program

Creator Information:
    created by [Aravind Kumar Vemula]
    twitter: xxxxxxxxx
    github: xxxxxxxxx
    web-link: xxxxxxxxx
"""

import cProfile
import os
import pstats
from datetime import datetime
from pstats import SortKey, Stats
import tracemalloc
import sys
import uuid
from terminaltables import AsciiTable


class LogiTyme:
    def __init__(self, env):
        self.env = env
        self.profiler = cProfile.Profile()
        self.tracemalloc = tracemalloc
        self.current_file_name = sys.argv[0].split("\\")[-1]
        self.filenames = []
        self.customProfile = None
        self.filePath = "/tmp/"
        self.fileName = ""

    """
    createDir:
        This will create a directory with tmp only in local server.
    """
    def createDir(self):
        if self.env == "local":
            if not os.path.exists("." + self.filePath):
                os.makedirs("." + self.filePath)

    """
    StartReport: 
        Is the feature used to start the process of logging the time for you python program.
    """
    def startReport(self):
        self.startTime = datetime.now()
        self.profiler.enable()
        self.tracemalloc.start()
        self.createDir()
    #
    # def exclude_function(self, action):
    #     if action == "exclude":
    #         self.profiler.disable()
    #     else:
    #         self.profiler.enable()

    """
    __Env_Suggestions:
        Based on the time taken by the program, this feature suggest which cloud provider is best to use, if you want to run in cloud.
    """
    def __env_suggestions(self, time_taken):
        if time_taken <= 300:
            return f"\t- Short tasks (less than 5 minutes):\n\t\t-- GCP (Cloud Functions, Compute Engine, GKE, Cloud Run) or AWS (Lambda, EC2, ECS, Step Function, Glue): \n\t\t\t Both are well-suited for tasks that complete quickly.\n\t\t-- Azure Functions (Consumption Plan, VM, AKS, Container Instances):\n\t\t\t Good choice for short tasks"
        elif time_taken > 300 and time_taken < 900:
            # aws ec2, ecs, eks, batch, gluex, step function
            # gcp compute entire, app engine, gke, cloud run
            return f"\t- Medium tasks (5 to 15 minutes):\n\t\t-- AWS Lambda: \n\t\t\t With a 15-minutes limit, AWS Lambda is ideal for tasks that require a bit more time.\n\t\t-- Azure Functions(Premium or Dedicated Plan, VM, AKS, Container Instance):\n\t\t\t These plans can handle longer execution time."
        elif time_taken >= 900 and time_taken < 3600:
            # aws ec2, ecs, eks, glue, step function
            # gcp compute engine, GKE, app engine (standard env)
            return f"\t- Long tasks (15 to 60 minutes):\n\t\t-- Azure Functions (Premium or Dedicated Plan, AKS, Container Instance, VM): \n\t\t\t Offers the flexibility to run tasks up tp 60 minsutes\n\t\t-- Docker Container:\n\t\t\t If any taks duration exceeds the limit of any serverless functions, Docker Conatiner have no timeout, allowing for long-running, complex workloads"
        elif time_taken >= 3600:
            # aws ec2, ecs, eks, glue, step function
            # gcp compute engine, gke, app engine(flexible env)
            # azure vm, aks, preimum or dedicated plan.
            return f"\t- Very Long tasks (over 60 minutes):\n\t\t-- Docker Container:\n\t\t\t If any taks duration exceeds the limit of any serverless functions, Docker Conatiner have no timeout, allowing for long-running, complex workloads"

    """
    __reportTempalte:
        This will create a template of the report with the logged data for each function and entire code. and save it as a txt file (if needed)
    """
    def __reportTemplate(
        self, total_time, memory_consumed, functions, inbuilt_functions,saveFile
    ):
        print("Report")
        report = f"Performance Analysis\n\n"
        report += f"1. Introduction:\n"
        report += f"""\tThis report presents the findings of performance analysis conducted on the python program '{self.current_file_name}'. This purpose of the analysis is to give insights of time consumed by the program and provide recommendations for optimizing the programs's performance\n\n"""
        report += f"2. Methodolgy:\n"
        report += f"""\tThe program was profiled using cprofile mmodile to collect data on exection time. The collected data was analyzed to identify functions consuming the most time.\n\n"""

        report += f"3. Results:\n"
        report += f"""\t- Started the program at: {self.startTime}\n\t- Ended the program at: {self.endTime}\n\t- Total Execution Time: {total_time} seconds\n\t- memory consumed: {round(memory_consumed,4)}MB\n\n"""
        report += f"4. Functions Results:\n"

        functions_table = [["Function Name", "Time Consumed"]]
        for i in functions.items():
            functions_table.append([i[0], str(round(i[1], 3)) + " secs"])
        function_table = AsciiTable(functions_table)
        report += f"""{function_table.table}\n\n"""

        report += "5. inBuilt-functions Time-Consumed Report:\n"
        inbuilt_data = [["Function Name", "Time Consumed"]]
        for i in inbuilt_functions.items():
            inbuilt_data.append([i[0], str(round(i[1], 3)) + " secs"])
        inbuilt_table = AsciiTable(inbuilt_data)
        report += f"""{inbuilt_table.table}\n\n"""

        report += f"6. Environment Suggestions:\n"
        report += f"{self.__env_suggestions(total_time)}\n\n"
        report += f"7. Code Optimization:\n"
        # max_time_consumed = max(functions, key=functions.get)
        functions_table = [["Function Name", "Time Consumed"]]
        functions = dict(
            sorted(functions.items(), key=lambda item: item[1], reverse=True)[:3]
        )
        report_function_max_time = ""
        c = 0
        for function in functions:
            if round(functions[function], 4) != 0:
                functions_table.append(
                    [function, str(round(functions[function], 4)) + " secs"]
                )
                c += 1
                report_function_max_time += f"""The above function "{function}" is in the {c} position for having highest amount of time in the entire program. Since the function took {round(functions[function],4)} secs is {round(functions[function],4)<300and "less then 300 seconds (i.e < 5 mins). The function is quite optimized"or"is more then 300 seconds (i.e >5 mins). Try to optimze the function a bit more to decrease the time consumed by code running on serverless or docker container"} \n"""
        function_table = AsciiTable(functions_table)
        report += function_table.table + "\n"
        report += report_function_max_time + "\n"
        report += "8. Conclusion:\n"
        report += f"\tThe analysis revealed areas for potential optimization in the Python program '{self.current_file_name}'. By implementing the recommendations outlined in this report, the program's performance can be improved, leading to better overall efficency"

        if(saveFile):
            with open("Generated Report for "+self.current_file_name+".txt","w") as f:
                f.writelines(report)
        else:
            print(report)

    """
    GenerateReport:
        This feature used to end the logging process and generate a report based on each function used in the code.
        Now this will start process the logged data and generate a report based on the time spent in each function used in your code.
        The generated report will provide insights into the performance if different functions
    """
    def GenerateReport(self,save=False):
        self.endTime = datetime.now()
        print("start: ", self.startTime)
        print("end: ", self.endTime)
        print(self.endTime - self.startTime,"curr")
        current, peak = self.tracemalloc.get_traced_memory()
        print(current / 10**6, " MB consumed")
        self.profiler.disable()
        # self.profiler.dump_stats("profile_results.prof")
        Stats(self.profiler).strip_dirs().sort_stats(
            SortKey.CALLS, SortKey.TIME
        ).print_stats()
        print("eeee")
        stats = Stats(self.profiler)
        res = str(stats)
        print(res,"resssssss")
        print(str(stats.print_stats()),stats.print_stats(),"strrrrrrrrrrrrrrrrrrr")
        # stats.print_stats()
        ttt = 0
        funcs = {}
        time_comsumed_inbuilt = {}
        for func, (cc, nc, tt, ct, callers) in stats.stats.items():
            ttt += round(tt, 3)
            if self.current_file_name in func[0]:
                funcs[func[2]] = round(ct, 3)
                print(ttt, "tttt")

            if "built-in" in func[2] and round(tt, 3) != 0.0:
                if func[2] not in time_comsumed_inbuilt:
                    time_comsumed_inbuilt[func[2]] = round(tt, 3)
                else:
                    time_comsumed_inbuilt[func[2]] += round(tt, 33)

        print(self.filenames,"fffff")
        for filename in self.filenames:
            stat1 = pstats.Stats("." + self.filePath + filename + ".prof" if self.env == "local" else self.filePath + filename + ".prof").sort_stats(
                "tottime"
            )
            stat1.print_stats()
            print("qqq")
            stats_total_tile = 0
            for func, (cc, nc, tt, ct, callers) in stat1.stats.items():
                stats_total_tile += round(tt, 3)
                # time_comsumed_by_other_files += round(tt,3)
                if "built-in" in func[2] and round(tt, 3) != 0.0:
                    if func[2] not in time_comsumed_inbuilt:
                        time_comsumed_inbuilt[func[2]] = round(tt, 3)
                    else:
                        time_comsumed_inbuilt[func[2]] += round(tt, 33)
            print(stats_total_tile, "stats_total_tile totla")
            funcs[filename] = stats_total_tile

        print(funcs, "funcs")
        print(ttt, "ttt")
        print(time_comsumed_inbuilt, "time_consumed_by_inbuilt")
        print("Total time taken: ", ttt)
        print(self.filenames, "filenames")
        # exit()
        for filename in self.filenames:
            os.remove("." + self.filePath + filename + ".prof" if self.env == "local" else self.filePath + filename + ".prof")
            # os.remove("." + self.filePath + filename + ".txt")
        self.filenames = []
        print(self.filenames, "filenames")
        funcs = dict(sorted(funcs.items(), reverse=True, key=lambda item: item[1]))
        time_comsumed_inbuilt = dict(
            sorted(
                time_comsumed_inbuilt.items(), reverse=True, key=lambda item: item[1]
            )
        )
        self.__reportTemplate(
            total_time=round(ttt, 3),
            memory_consumed=current / 10**6,
            functions=funcs,
            inbuilt_functions=time_comsumed_inbuilt,
            saveFile=save
        )


    """
    LogiFunctStart & LogiFuncEnd:
        This feature is used to log time for custom code.
    """
    def LogiFuncStart(self, name="default"):
        if name == "default":
            name = str(uuid.uuid4())
            self.fileName = name
        else:
            if(os.path.exists("." + self.filePath + name + ".prof" if self.env == "local" else self.filePath + name + ".prof")):
                name = name + "_" + str(uuid.uuid4())
                self.fileName = name
            else:
                self.fileName = name
        self.customProfile = cProfile.Profile()
        self.customProfile.enable()
        self.filenames.append(name)

    def LogiFuncEnd(self):
        name = self.fileName
        Stats(self.customProfile).strip_dirs().sort_stats("ncalls").dump_stats(
            "." + self.filePath + name + ".prof" if self.env == "local" else self.filePath + name + ".prof"
        )
        self.customProfile.disable()
        Stats(self.customProfile).strip_dirs().sort_stats("ncalls").print_stats()
        self.customProfile = None
        self.fileName = ""
        self.profiler.enable()
