from dataclasses import dataclass
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

@dataclass
class Prediction:
    value: float
    r2_score: float
    slope: float
    intercept: float
    mean_absolute_error: float

    def __str__(self):
        return(f"Prediction: {self.value:.2f} | {self.r2_score:.2f}")
    
def make_prediction(input: list[float], output: list[float], input_value: float, plot: bool = False) -> Prediction:
    if len(input) != len(output):
        raise Exception("Length of the input should be equal to output!")
    
    df = pd.DataFrame({'inputs': input, 'outputs': output})

    x = np.array(df['inputs']).reshape(-1,1)
    y = np.array(df['outputs']).reshape(-1,1)

    train_x , test_x, train_y , test_y = train_test_split(x ,y, random_state=0, test_size=.20)

    model = LinearRegression()
    model.fit(train_x, train_y)

    y_predictions = model.predict([[input_value]])
    y_line = model.predict(x)

    y_test_predictions = model.predict(test_x)

    if plot:
        plot_graph(input=x, output=y, y_line=y_line)
    
    return Prediction(
        value=y_predictions[0][0],
        r2_score=r2_score(test_x, y_test_predictions),
        slope=model.coef_[0][0],
        intercept=model.intercept_[0],
        mean_absolute_error=mean_absolute_error(test_x, y_test_predictions),
    )

def plot_graph(input: list[float], output: list[float], y_line):
    plt.scatter(input, output, s=12)
    plt.xlabel("Input")
    plt.ylabel("Output")
    plt.plot(input, y_line, color='r')
    plt.show()

if __name__ == '__main__':
    print(make_prediction(
        input=[1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10],
        output=[10, 20, 30, 35, 50, 40, 70, 72, 90, 97],
        input_value=20,
        plot=True)
)
