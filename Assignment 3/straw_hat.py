'''
    This file contains the class definition for the StrawHat class.
'''

import crewmate
import heap
import treasure

'''
    This file contains the class definition for the StrawHat class.
'''


def comparison_fn1_crew(crew1,crew2):
    return crew1.key_for_crew < crew2.key_for_crew



class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        

        # Write your code here
        self.no_of_crew = m
        self.init_array_crewmates = []
        for i in range(m):
            temp = CrewMate()
            self.init_array_crewmates.append(temp)
        self.heap_crewmates = Heap(comparison_fn1_crew,self.init_array_crewmates)
        self.total_treasures_present = 0
        self.treasure_array = []


    
    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
       

        reqd_crewmate = self.heap_crewmates.myheap_array[0]
        reqd_crewmate.treasures.append(treasure)
        reqd_crewmate.key_for_crew = max(reqd_crewmate.key_for_crew, treasure.arrival_time) + treasure.size
        self.heap_crewmates.Heapify(0)
        self.total_treasures_present += 1
        self.treasure_array.append(treasure)
            

    
    def get_completion_time(self):
        all_treasures = []

        if(self.total_treasures_present < self.no_of_crew):
           
            for i in range(self.total_treasures_present):
                reqd = self.treasure_array[i]
                reqd.completion_time = reqd.size + reqd.arrival_time
                all_treasures.append(reqd)
        
        else:
            for crewmate in self.heap_crewmates.myheap_array:
                if not crewmate.treasures:
                    continue
                
                all_treasures += crewmate.get_completion_helper()

        all_treasures.sort(key=lambda x: x.id)
        return all_treasures


