
# Big Data overview
* What is Big Data?
* Explanation of Hadoop, MapReduce, and Spark
* Local versus Distributed Systems
* Overview of Hadoop Ecosystems
* Overview of Spark

## What is Big Data
Big Data is a combination of structered, semistructered and unstructered data collected by organizations that can be mined for information and used in machine learning projects, predictive modeling and other advanced analytics applications.   
Big Data is often described by these 5 characteristics:
* Volume: the size and amounts of Big Data that companies manage and analyze
* Value: the most important "V" from the perspective of the business, the value of big data usually comes from insight discovery and pattern recognition that lead to more effective operations, stronger customer relationships
* Variety: the diversity and range of different data types
* Velocity: the speed at which companies receive, store and manage data
* Veracity: the truth or accuracy of data and information assets

### What can we do if we have a larger set of data?
* Try using SQL database to move storage onto hard drive instead of RAM
* or use a distributed system, that distributes the data to multiple machines/computer. And this where Spark coming to play.

### Local versus Distributed
#### Local system
* Local system - where we use single machine, single computer and uses the same RAM, the same Hard drive 
* You will be limited how many cores you have in a local system 
* So a local process will use the computation resources of a single machine
#### Distributed system 
* Distributed system - where we have one main computer called master node, where data and calculations distributed among other computers 
* In distributed system you can leverage a power among weaker machines to eventually have more cores and more capabilites than even a strong local single machine
* Distributed process has access to the computational resources across a number of machines connected through some sort of network
* After a certain point, it is easier to scale out many lower CPU machines, than to try to scale up to a single machine with a high CPU. You can just add more machines
* Also included fault tolerance, if one machine fails, the whole network can still go on
* Fault tolerance, if one machine fails, the whole network can still go on. Fault tolerance is a fundemental idea where you are going to be replicating your data across multiple machines.

## Hadoop
* Hadoop is a way to distribute very large files across multiple machines
* It uses the Hadoop Distributed File System (HDFS)
* HDFS allows a user to work with large data sets across a distributed system
* HDFS also duplicates blocks of data for fault tolerance, which is the idea if one machine goes down in your system, your data is duplicated on some other machine.
* it also uses what's known as MapReduce, and MapReduce allows computations on that distributed data
* MapReduce is used to distribute a computational task to a distributed data set; 
### Distributed Storage - HDFS
* Name node (Master Node) - has its own CPU, RAM - controls the process of either distributing to storage or to calculations through slave nodes (Data Node)
* HDFS will use blocks of data, with a size of 128MB by default
* Each of these blocks is replicated 3 times
* The blocks are distributed in a way to support fault tolerance
* Smaller blocks provide more parallelization during processing
### MapReduce
* MapReduce is a way of splitting a computation task to a distributed set of files (such as HDFS)
* It consists of a Job Tracker and multiple Task Trackers
* The Job Tracker sends code to run on the Task Trackers
* The Task trackers allocate CPU and memory for the tasks and monitor the tasks on the worker nodes

## Spark 
* What is Spark
* Spark vs MapReduce
* Spark RDD
* Spark DataFrames
### What is Spark
* Spark is one the latest technologies used to quickly and easy handle Big Data
* It is an open source project on Apache
* You can think of Spark as a flexible alternative to MapReduce
###





