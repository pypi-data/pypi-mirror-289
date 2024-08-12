import pandas as pd
import numpy as np
import sys
def topsis(input_file,weights,impacts,outputfile):
    try:
        data=pd.read_csv(input_file)
        if data.shape[1] < 3:
            raise ValueError("Input file must contain three or more columns.")
        df=data.iloc[:,1:]
        if not df.apply(pd.api.types.is_numeric_dtype).all():
            raise ValueError("Columns from 2nd to last must contain numeric values only.")
        if len(weights) !=len(impacts)!= df.shape[1]:
            raise ValueError("Number of weights and impacts must match the number of criteria (from 2nd to last columns).")
        df=df.values
        normalized_df=df/np.sqrt((df**2).sum(axis=0))
        weighted_df=weights*normalized_df
        ideal_best=np.zeros(weighted_df.shape[1])
        ideal_worst=np.zeros(weighted_df.shape[1])
        
        for i in range(len(impacts)):
            if impacts[i]=='+':
                ideal_best[i]=np.amax(weighted_df[:,i])
                ideal_worst[i]=np.amin(weighted_df[:,i]) 
            elif impacts[i]=='-':
                ideal_best[i]=np.amin(weighted_df[:,i])
                ideal_worst[i]=np.amax(weighted_df[:,i])
            else:
                raise ValueError("Wrong input to impact.Use '+' or '-' ")    
    
        distance_to_idealbest=np.sqrt(((weighted_df-ideal_best)**2).sum(axis=1))
        distance_to_idealworst=np.sqrt(((weighted_df-ideal_worst)**2).sum(axis=1))
    
        performance_score=distance_to_idealworst/(distance_to_idealbest+distance_to_idealworst)
        
        data['Performance_Score']=performance_score
        data['Rank']=data['Performance_Score'].rank(ascending=False)
        
        data.to_csv(outputfile,index=False)
    except FileNotFoundError:
        print(f"Input file {input_file} not found")
    except ValueError as ve:
        print(f"Input error:{ve} ")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")    
        
if __name__ == "__main__":
    try:
        if len(sys.argv) != 5:
            raise ValueError("Incorrect number of parameters. Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        
        input_file = sys.argv[1]
        weights = list(map(float, sys.argv[2].strip('"').split(',')))
        impacts = sys.argv[3].strip('"').split(',')
        result_file = sys.argv[4]
        
        topsis(input_file, weights, impacts, result_file)
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    