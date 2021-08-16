# RouteFinder
What is the fastest route someone could take to reach every train station in Sydney?


## Brainstorming for algorithm:

### Relevant Research:
https://www.sciencedirect.com/science/article/abs/pii/S1570667213601245

### Stupid naive:
find a way to recursively iterate through all options (astronomical complexity)

### Naive greedy:
start at a train station





### how to handle the data structure?



### Exact or heuristic? 

#### How to encode?

the search space is really large

Option 1:
If a train goes to stations A-->B-->C, then you need to have the following 'trips' available:
- A--> B
- A--> C
- B--> C
for a trip $n$ long, you need $n+(n-1)+...+2+1 = O(n^2)$.

Which isn't terrible, but it's a pretty bad multiplier (if a train route has on avg 30 stops, it's a 30x multiplier)

Option 2 (better):
break up each route into chunks, so if the train line is A--B--C--D--E, and a route is A-->B-->C-->E, then this would be broken up into A-->B, B-->C, C-->E, each with its own start and stop time.

### Simple greedy approach:

compute a look-up table of the edge distance of stations from one another

at a station, look for the 'nearest' unvisited station, and compute the shortest route to that station

how to compute 'nearest'? a basic approach would be to look-up the edge distance between the stations

### Genetic greedy approach

### Idea: ignore train stations where you don't have to make a decision

could just look at the 'branches'

### Even better idea: start things off by ignoring the trains entirely

compute the fastest traversal of the graph given by the train network

## Current 'best' idea:

Identify "important" stations (currently: > 2 stations directly adjacent)

build a simplified graph of the overall network which only includes 'important' stations, where you put an edge between important stations 