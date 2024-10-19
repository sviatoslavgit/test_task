import json
import os
from typing import List, Dict

''' 
    Using a dictionary in order to store responses to ensure code readability, low memory usage and efficiency O(1). Opposing to the OOP style solution which is significantly more complicated 
    solution. The OOP styled solution would have been more useful provided we had more complicated requirements like more different methods, complicated inheritance hierarchy etc.
'''

def solution() -> str:
    animal_sounds: Dict[str, str] = {
        "dog": "bark",
        "cat": "meow",
        "cow": "moo",
        "rat": "pipi",
        "alien": "KILL"
    }
    
    results: List[str] = []
    file_path = 'test.json'
    # Basic error handling
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File '{file_path}' not found!")
            
        if os.path.getsize(file_path) == 0:
            raise ValueError(f"File '{file_path}' is empty!")
        
        with open(file_path, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON format: {str(e)}")
        
        if not isinstance(data, list):
            raise ValueError("JSON file should contain an array of objects!")
        
        if not data:
            raise ValueError("JSON array is empty!")
        
        for index, item in enumerate(data, 1):
            try:
                if not isinstance(item, dict):
                    raise ValueError(f"Item #{index} is not an object!")
                
                if 'field1' not in item:
                    raise ValueError(f"Item #{index} missing required 'field1' field!")
                    
                if 'animal' not in item:
                    raise ValueError(f"Item #{index} missing required 'animal' field!")

                if item['field1'] != "value1":
                    raise ValueError(f"Item #{index} has invalid 'field1' value! Expected 'value1', got '{item['field1']}'")
                
                animal = item['animal']
                
                if animal not in animal_sounds:
                    results.append(f"Warning! Item #{index} - Animal: {animal} -> Unknown animal type")
                    continue
                #Storing one of possible outputs
                sound = animal_sounds[animal]
                results.append(f"Item #{index} - Animal: {animal} -> Sound: {sound}")
                
            except KeyError as e:
                results.append(f"Error in item #{index}: Missing key {str(e)}")
            except Exception as e:
                results.append(f"Error processing item #{index}: {str(e)}")
        
        if not results:
            raise ValueError("No valid records found in the file!")
        
        return "\n".join(results)
        
    except FileNotFoundError as e:
        return f"Error: {str(e)}"
    except ValueError as e:
        return f"Error: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

def main():
    #output of the result
    print("\n=== Animal Sounds Processor ===\n")
    result = solution()
    print(result)
    print("\n======== End of Process =======")

if __name__ == "__main__":
    main()