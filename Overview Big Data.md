
Classic Database - using SQL database to move storage onto hard drive instead of RAM.
or use a distributed system, that distributes the data to multiple machines/computer.

Master node.
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
* MapReduce allows computations on that data. to distribute a computational task to a distributed data set; 

Name node (controlls):
1. Data node
2. Data node
3. Data mode

Spark
* Spark is one of the latest technologies being used to quickly and easily handle Big Data
