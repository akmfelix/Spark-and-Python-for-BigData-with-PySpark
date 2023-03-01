
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



* Big Data is a collection of data that is huge in volume, yet growing exponentially with time. It is a data with so large size and complexity that none of traditional data management tools can store it or process it efficiently. Big data is also a data but with huge size.

Big Data
* A local process will use the computation resources of a single machine; 
* A distributed process has access to the computational resources across a number of machines connected throug a network;
* It is easier to scale out to many lower CPU machines, than try to scale up to a single machine with a high CPU
* Distributed machines also have the advantage of easily scaling, you can just add more machines;
* Fault tolerance, if one machine fails, the whole network can still go on.


Hadoop
* Hadoop is a way to distribute very large files across multiple machines;
* It uses the Hadoop Distributed File System (HDFS);
* HDFS allows a user to work with large tat sets;
* HDFS also duplicates blocks of data for fault tolerance;
* uses MapReduce;
* MapReduce allows computations on distributed data. MapReduce is used to distribute a computational task to a distributed data set; 

Distributed STORAGE
Master where data and calculations distributed onto other computers.
Name node (master node) controls the process od distr storage, calculations to the other nodes- slave nodes:
1. Data node
2. Data node
3. Data mode

Spark
* Spark is one of the latest technologies being used to quickly and easily handle Big Data

Distributed Storage - HDFS
* HDFS will use blocks of data, with a size of 128MB by default
* Each of these blocks is replicated 3 times
* The blocks are distributed in a way to support fault tolerance
* Smaller blocks provide more parallelization during processing
* Multiple copies of a block prevent loss of data due to a failure of a node

Map Reduce
* MapReduce is a way of splitting a computation task to a distributed set of files (HDFS)
* It consists of a Job Tracker and miltiple Task Trackers
* Job Trackers sends code to run on the Task Trackers
* The Task Trackers allocate CPU and memory for the tasks and monitor the tasks on the worker nodes. 

SPARK:
* You can think of Spark as a flexible alternative to MapReduce
* Spark can use data stored in a variety of formats: Cassandra, AWS S3, HDFS and more

 Spark vs MapReduce
 * MapReduce requires files to be stored in HDFS, Spark does not
 * Spark also can perform operations up to 100x faster than MapReduce
 * MapReduce writes most data to disk after each map and reduce operation
 * Spark keeps most of the data in memory after each transformation
 * Spark can spill over to disk if the memory is filled


