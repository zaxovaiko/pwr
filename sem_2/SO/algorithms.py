from random import randint

def c_scan(queue, max):
    head = queue[0]
    requests = queue[::]

    print("---- C-SCAN Disk Scheduling Algorithm ----")
    print("Queue is:", queue)
    print("Head is on", head)

    requests.sort()

    # Find the nearest end and cut lists
    if head <= abs(head - max):
        start = ([0] + requests[0:requests.index(head) + 1])[::-1]
        end = (requests[requests.index(head) + 1::] + [max])[::-1]
    else:
        start = requests[requests.index(head):] + [max]
        end = [0] + requests[0:requests.index(head):]

    requests = start + end
    res = []
    for i in range(1, len(requests)):
        res.append(abs(requests[i - 1] - requests[i]))

        # Skip difference between start and end
        if (requests[i-1] == max and requests[i] == 0) or (requests[i-1] == 0 and requests[i] == max):
            res[i - 1] = 0
        print('From {:>3} to {:>3} with {:>3} seeks'.format(requests[i - 1], requests[i], res[i - 1]))

    return sum(res)

  
def fcfs(queue):
    print("---- FCFS Disk Scheduling Algorithm ----")
    print("Queue:", queue)
    print("Head is on:", queue[0])

    res = []
    for i in range(1, len(queue)):
        # Count diff between each next request and write it to list
        res.append(abs(queue[i - 1] - queue[i]))
        print('From {:>3} to {:>3} with {:>3} seeks'.format(queue[i - 1], queue[i], res[i - 1]))

    # Count total disk's head movements
    return sum(res)
  

def scan(queue, max):
    requests = queue[::]
    head = requests[0]

    print("---- SCAN Disk Scheduling Algorithm ----")
    print("Queue is:", requests)
    print("Head is on:", head)

    requests.sort()

    # Find the nearest end and cut lists
    if head <= abs(head - max):
        # input:  [15, 46, 53, 73, 84]
        # output: [15, 0] [46, 53, 73, 84]
        start = ([0] + requests[0:requests.index(head) + 1])[::-1]
        end = requests[requests.index(head) + 1::]
    else:
        # input:  [15, 26, 37, 69, 87]
        # output: [87, max] [69, 37, 26, 15]
        start = requests[requests.index(head):] + [max]
        end = (requests[0:requests.index(head):])[::-1]

    request = start + end
    res = []
    for i in range(1, len(request)):
        res.append(abs(request[i - 1] - request[i]))
        print('From {:>3} to {:>3} with {:>3} seeks'.format(request[i - 1], request[i], res[i - 1]))

    return sum(res)  
 

def scan_edf(queue, max):
    # Sort by arrival time and then by deadline
    requests = sorted(queue[::], key=lambda x: x[:2])
    head = min(requests, key=lambda a: a[0])[2]

    print("---- EDF-SCAN Real-time Disk Scheduling Algorithm ----")
    print("Queue:", requests)
    print("Head is on:", head)

    # Filters list by arrival time and then by deadline (example):
    e = []
    temp = []
    last_index = 0
    for i in range(len(requests) - 1):
        temp.append(requests[i])
        # Save sublist while next one isn't different
        if requests[i][0] != requests[i + 1][0]:
            last_index = requests.index(requests[i])
            e.append(temp)
            temp = []

    # Add last part
    # Map list by third value in sublist
    # Copy list to previous name
    e.append(requests[last_index + 1:])
    for i in range(len(e)):
        e[i] = list(map(lambda x: x[2], e[i]))
    requests = e[::]
    # Format by arrival time
    print("Formatted list:", requests)

    # Set initial direction in which disk's head moves ('r' or 'l')
    dr = 'l' if head <= abs(head - max) else 'r'

    seek = 0
    for req in requests:
        request = [head] + req[::]
        request.sort()

        # Cuts request list by two parts
        if dr == 'r':
            start = request[request.index(head):] + [max]
            end = (request[0:request.index(head):])[::-1]
            dr = 'l'
        elif dr == 'l':
            start = ([0] + request[0:request.index(head) + 1])[::-1]
            end = request[request.index(head) + 1::]
            dr = 'r'

        # Update head position
        request = start + end
        head = request[-1]

        # Count gap between each request in current deadline
        res = []
        for i in range(1, len(request)):
            res.append(abs(request[i - 1] - request[i]))
            print('From {:>3} to {:>3} with {:>3} seeks'.format(request[i - 1], request[i], res[i - 1]))

        seek += sum(res)
    return seek


 def sstf(queue):
    requests = queue[::]
    head = requests[0]

    print("---- SSTF Disk Scheduling Algorithm ----")
    print("Queue:", requests)
    print("Head is on:", head)

    res = []
    requests.sort(key=lambda x: abs(head - x))  # Sort by lower distance from the head

    for i in range(1, len(requests)):
        res.append(abs(requests[i - 1] - requests[i]))  # Count diff between each next request and write it to list
        print('From {:>3} to {:>3} with {:>3} seeks'.format(requests[i - 1], requests[i], res[i - 1]))

    return sum(res)
  
  
# MAX value of disk head position
# Generate queue with 5 random requests
MAX = 99
queue = [randint(0, MAX) for i in range(20)]

print("Total movements:", fcfs(queue), '\n')
print("Total movements:", sstf(queue), '\n')
print("Total movements:", scan(queue, MAX), '\n')
print("Total movements:", c_scan(queue, MAX), '\n')

# Random list with arrival time, deadline and position
# Change range to get more or less random values
queue = [[randint(0, 3), randint(1, 10), randint(0, MAX)] for _ in range(5)]
print("Total movements:", scan_edf(queue, MAX))