'''
    Python file to implement the class CrewMate
'''

import crewmate
import heap
import treasure

def comparison_fn2_treasure(treasure1, treasure2):

    priority1 = (treasure1.arrival_time + treasure1.size, treasure1.id)
    priority2 = (treasure2.arrival_time + treasure2.size, treasure2.id)
    
    # Return the comparison (min-heap based on this tuple)
    return priority1 < priority2


class CrewMate:
    '''
    Class to implement a crewmate
    '''
    
    def __init__(self):
        '''
        Arguments:
            None
        Returns:
            None
        Description:
            Initializes the crewmate
        '''
        self.key_for_crew = 0  #comparing total completion time of all treasure for a crewmate is same as comparing its load (directly proportional)
        self.treasures = []

    def get_completion_helper(self):
        all_treasures = []
        
        if not self.treasures:
            return all_treasures
        
        current_time = self.treasures[0].arrival_time
        heap_treasure = Heap(comparison_fn2_treasure, [])

        # Insert the first treasure
        first_treasure = Treasure(self.treasures[0].id, self.treasures[0].size, self.treasures[0].arrival_time)
        heap_treasure.insert(first_treasure)

        for i in range(1, len(self.treasures)):
            curr = heap_treasure.top()
            next_time = self.treasures[i].arrival_time
            available_time = next_time - current_time
            
            while curr and available_time >= curr.size:
                p = heap_treasure.extract()
                current_time += p.size  # Update the current time before setting completion
                p.completion_time = current_time  # Correct time
                p.size = 0
                all_treasures.append(p)
                curr = heap_treasure.top()
                available_time = next_time - current_time

            if curr:
                curr.size -= available_time  # Reduce remaining size by available time
                heap_treasure.Heapify(0)  # Restore heap order
            current_time = next_time
            
            temp = Treasure(self.treasures[i].id, self.treasures[i].size, self.treasures[i].arrival_time)
            heap_treasure.insert(temp)
        
        # Process remaining treasures in heap
        while heap_treasure.top():
            p = heap_treasure.extract()
            current_time += p.size  # Ensure completion time reflects the correct time
            p.completion_time = current_time
            all_treasures.append(p)

        return all_treasures
             



                



            
            
        



