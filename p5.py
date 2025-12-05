FNAME = "in5.txt"

# parse the range lines in the first chunk    
def parse_line(line):
    return [int(i) for i in line.split('-')]

fresh_ranges, ingredients = [chunk.splitlines() for chunk in open(FNAME).read().split('\n\n')]

fresh_ranges = [parse_line(line) for line in fresh_ranges]
ingredients = [int(i) for i in ingredients]

def is_fresh(ingredient):
    for a, b in fresh_ranges:
        if a <= ingredient <= b:
            return True
    return False
    
part1 = sum(is_fresh(i) for i in ingredients)
print("Part 1:", part1) # 674

# take two intervals [a, b], [c, d] and merge them into a single interval [e, f]
# this is only possible if they intersect--return sentinel value False when impossible
def merge(a, b, c, d):
    if a <= c <= d <= b: # first interval encloses second
        return (a, b)
    elif c <= a <= b <= d: # second interval encloses first
        return (c, d)
    elif a <= c <= b <= d: # partially overlapping 1
        return (a, d)
    elif c <= a <= d <= b: # partially overlapping 2
        return (c, b)
    else: # non-overlapping
        return False
        
 # basic idea: we want to merge any ranges that can be merged,
 # until we have a final list of non-overlapping ranges
 # so we queue up all the ranges
 # one at a time, we move them to final_ranges
 # except if they overlap with one of the extant final_ranges
 # in which case we merge them, delete the instance in final_ranges
 # then move the merged range to the expand queue, 
 # since it may still overlap other ranges
 
# set up our data structures
expandq = fresh_ranges
final_ranges = [expandq.pop(0)]

# keep processing until there's nothing left to process...
while expandq:
    
    # grab the next one
    next_range = expandq.pop(0)
    
    # see if the range intersects with any extant ranges
    for r in final_ranges:
        x = merge(*r, *next_range)
        if x:
            expandq.append(x)
            final_ranges.remove(r)
            break
            
    # if we DIDN'T match any existing ranges,
    # this one is ready to move to final_ranges
    if not x:
        final_ranges.append(next_range)

# sum the size of all ranges
part2 = sum(b - a + 1 for a, b in final_ranges)
print("Part 2:", part2) # 352509891817881
