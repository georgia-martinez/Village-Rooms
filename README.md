# The Village Room Rankings (CWRU)

Gives a ranking of the rooms in The Village based on your preferences. 

DISCLAIMER: Only rooms included in the input csv file are included in the rankings. The included rooms.csv does NOT include every room in The Village. It contains 4-person rooms excluding the ones facing 115th street or on the 1st floor. Feel free to add more rooms to the csv.  

## Set up

```
pip install -r requirements.txt
```

## How to run

Set up the config.yaml file to customize the ranking system.

The `priority` field defines which room attributes to prioritize when calculating rankings. For example, if you wanted to sort the rooms by house number first, floor number second, and view last, you would put the following in the config.yaml:

```
priority: [house, floor, view]
```

Then for each attribute, you should put your desired order. For example, you could rank the houses like this:

```
house: [4, 5, 6, 7, 3, 2, 1]
```

Note that from left to right, it goes from MOST wanted to LEAST wanted. So from the above example, house 4 is the top pick and house 1 is the last pick.

## Room attributes

Below are descriptions of each room attribute you can sort by. Feel free to modify the code to add or change attributes. Note that the spelling is case sensitive. 

`house`: the house number (House 1, House 2, ..., House 7)

`view`: view from the windows

`floor`: floor number

`large`: the size of the common room 

## Other config settings

`input`: csv file with the initial room data

`output`: name for output csv file with the rankings