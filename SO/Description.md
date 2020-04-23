# Disk scheduling algorithms

## FCFS

FCFS is the simplest of all the Disk Scheduling Algorithms.
In FCFS, the requests are addressed in the order they arrive in the disk queue.

Advantages:

   - Every request gets a fair chance  
   - No indefinite postponement
   
Disadvantages:
   - Does not try to optimize seek time  
   - May not provide the best possible service

## SSTF

In SSTF (Shortest Seek Time First), requests having shortest seek time are executed first.
So, the seek time of every request is calculated in advance in queue and then they are
scheduled according to their calculated seek time. As a result, the request near the disk
arm will get executed first. SSTF is certainly an improvement over FCFS as it decreases
the average response time and increases the throughput of system.

Advantages:  

   - Average Response Time decreases
   - Throughput increases
    
Disadvantages:  

   - Overhead to calculate seek time in advance
   - Can cause Starvation for a request if it has higher seek time as compared to incoming requests
   - High variance of response time as SSTF favours only some requests

## SCAN

In SCAN algorithm the disk arm moves into a particular direction
and services the requests coming in its path and after reaching the end
of disk, it reverses its direction and again services the request arriving
in its path. So, this algorithm works like an elevator and hence also
known as elevator algorithm. As a result, the requests at the midrange are
serviced more and those arriving behind the disk arm will have to wait.

Advantages:

   - High throughput
   - Low variance of response time
   - Average response time
   
Disadvantages:

   - Long waiting time for requests for locations just visited by disk arm

## C-SCAN

In SCAN algorithm, the disk arm again scans the path that has been scanned,
after reversing its direction. So, it may be possible that too many requests
are waiting at the other end or there may be zero or few requests pending
at the scanned area. These situations are avoided in CSAN algorithm in which
the disk arm instead of reversing its direction goes to the other end of the
disk and starts servicing the requests from there. So, the disk arm moves in
a circular fashion and this algorithm is also similar to SCAN algorithm and
hence it is known as C-SCAN (Circular SCAN).

Advantages:

   - Provides more uniform wait time compared to SCAN

## REAL-TIME DISK SCHEDULING ALGORITHMS
### SCAN-EDF

The Earliest Deadline First algorithm is an
analog of FCFS. Requests are orders according to
deadline and the request with the earliest deadline is
serviced first. Assigning priorities to transactions an
Earliest Deadline policy minimizes the number of late
transactions in systems operating under low or
moderate levels of resources and data contention. This
is due to Earliest Deadline steeply degrades in an
overloaded system.

----

For better understanding use [this explanation](http://www.cs.iit.edu/~cs561/cs450/disksched/disksched.html) or [this one](https://www.ijltemas.in/DigitalLibrary/Vol.2Issue3/112-120.pdf).