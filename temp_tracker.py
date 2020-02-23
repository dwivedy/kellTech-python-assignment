from collections import Counter 
class TempTracker:
    

     'TempTracker class for temperature tracking.'
     def __init__(self):
        self._temperatureRecord =[] 

      #insert temperature into list
     def insert(self,temperature):
        if (temperature<0 or temperature >150):
            raise ValueError("Temperature range between 0\xb0C and 150\xb0C")
        self._temperatureRecord.append(temperature)
        

      #get max temperature from list   
     def get_max(self):
          return max(self._temperatureRecord)
        
     #get min temperature from list   
     def get_min(self):
       return min(self._temperatureRecord)

     #get mean temperature from list   
     def get_mean(self):
        return sum(self._temperatureRecord) / len(self._temperatureRecord) 

    #get mode temperature from list      
     def get_mode(self):
         data = Counter(self._temperatureRecord)
         get_mode = dict(data)
         mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
         if len(mode) == len(self._temperatureRecord):
             return "No mode in the list"
         else:
             return min(mode)
  

     #insert multiple temperature into list, utility method
     def insertRecords(self):
         temperature=12
         increment=7
         for i in range(1, 12):
             self.insert(temperature)
             temperature=temperature+increment
             
             
             



       
if __name__ == '__main__':

    #object instantiation
    tempTracker = TempTracker()
    
    #insert multiple temperature
    tempTracker.insertRecords()
    
    #print(tempTracker._temperatureRecord)
    #print(sum(tempTracker._temperatureRecord))
    
    #max
    print("Max temperature: ")
    print(tempTracker.get_max())
    
    #min
    print("Min temperature: ")
    print(tempTracker.get_min())
    #mean
    print("Mean temperature: ")
    print(tempTracker.get_mean())
    #mode
    tempTracker.insert(1 )
    tempTracker.insert(2 )
    tempTracker.insert(2)
    tempTracker.insert(4)
    tempTracker.insert(5)
    print("Mode temperature: ")
    print(tempTracker.get_mode())
    
