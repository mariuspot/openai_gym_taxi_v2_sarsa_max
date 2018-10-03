# Implement of Sarsa MAX (Q-LEarning) and Sarsa Expected for Taxi V2 from Open AI Gym

Original Paper: 

    https://arxiv.org/pdf/cs/9905014.pdf

Open AI Gym: 

    https://gym.openai.com/
    https://github.com/openai/gym
    
_Open AI Gym considers it solved at an average reward of 9.7, but this seems high considering the shortest scenario is 6 actions and the longest is 18, giving a reward between 3 and 15 for a perfect plan._

## Results
* BAR = Best Average Result
* EC = Epsilon Change

|BAR|EC|Alpha|Gamma|Type|
|-|-|-|-|-|
|9.59|0.45|0.05|0.85|Sarsa expected|
|9.56|0.75|0.1|0.9|Sarsa expected|
|9.52|0.45|0.05|0.95|Sarsa expected|
|9.51|0.75|0.15|0.95|Sarsa expected|
|9.46|0.6|0.2|0.95|Sarsa expected|
|9.44|0.75|0.1|1.0|Sarsa max|
|9.44|0.6|0.1|0.9|Sarsa expected|
|9.41|0.9|0.2|1.0|Sarsa expected|
|9.4|0.75|0.1|0.95|Sarsa max|
|9.39|0.75|0.05|0.85|Sarsa max|
|9.39|0.9|0.15|1.0|Sarsa max|
|9.39|0.45|0.2|0.95|Sarsa max|
|9.39|0.75|0.2|0.9|Sarsa max|
|9.38|0.9|0.05|0.9|Sarsa max|
|9.37|0.75|0.1|1.0|Sarsa expected|
|9.37|0.6|0.1|0.9|Sarsa max|
|9.37|0.75|0.1|0.85|Sarsa expected|
|9.37|0.45|0.1|0.85|Sarsa max|
|9.36|0.6|0.05|0.95|Sarsa max|
|9.36|0.9|0.05|0.85|Sarsa expected|
|9.36|0.6|0.1|1.0|Sarsa max|
|9.36|0.9|0.15|0.9|Sarsa max|
|9.36|0.6|0.15|0.9|Sarsa max|
|9.34|0.75|0.05|0.95|Sarsa expected|
|9.34|0.6|0.05|0.9|Sarsa max|
|9.34|0.9|0.1|0.9|Sarsa expected|
|9.34|0.45|0.1|0.9|Sarsa expected|
|9.34|0.6|0.15|0.85|Sarsa expected|
|9.33|0.45|0.1|0.95|Sarsa expected|
|9.33|0.45|0.15|0.9|Sarsa max|
|9.32|0.6|0.05|1.0|Sarsa max|
|9.32|0.45|0.05|1.0|Sarsa expected|
|9.32|0.9|0.15|0.9|Sarsa expected|
|9.32|0.9|0.15|0.85|Sarsa max|
|9.31|0.6|0.05|0.85|Sarsa max|
|9.31|0.9|0.1|0.95|Sarsa max|
|9.31|0.9|0.1|0.95|Sarsa expected|
|9.31|0.6|0.1|0.85|Sarsa expected|
|9.31|0.6|0.15|0.85|Sarsa max|
|9.31|0.75|0.2|0.9|Sarsa expected|
|9.3|0.6|0.1|0.95|Sarsa max|
|9.3|0.45|0.15|0.95|Sarsa expected|
|9.29|0.6|0.05|0.95|Sarsa expected|
|9.29|0.6|0.05|0.9|Sarsa expected|
|9.29|0.75|0.05|0.85|Sarsa expected|
|9.29|0.9|0.15|0.95|Sarsa max|
|9.29|0.45|0.15|0.95|Sarsa max|
|9.29|0.45|0.15|0.9|Sarsa expected|
|9.29|0.45|0.2|1.0|Sarsa max|
|9.29|0.45|0.2|0.85|Sarsa expected|
|9.28|0.45|0.05|0.9|Sarsa expected|
|9.28|0.75|0.1|0.9|Sarsa max|
|9.28|0.9|0.1|0.85|Sarsa max|
|9.28|0.6|0.1|0.85|Sarsa max|
|9.28|0.75|0.15|1.0|Sarsa expected|
|9.28|0.45|0.15|0.85|Sarsa expected|
|9.28|0.9|0.2|0.95|Sarsa expected|
|9.28|0.75|0.2|0.95|Sarsa expected|
|9.28|0.6|0.2|0.85|Sarsa expected|
|9.28|0.45|0.2|0.85|Sarsa max|
|9.27|0.75|0.05|0.9|Sarsa max|
|9.27|0.45|0.05|0.9|Sarsa max|
|9.27|0.6|0.15|0.9|Sarsa expected|
|9.27|0.45|0.15|0.85|Sarsa max|
|9.27|0.75|0.2|1.0|Sarsa expected|
|9.27|0.6|0.2|1.0|Sarsa max|
|9.26|0.45|0.05|0.95|Sarsa max|
|9.26|0.9|0.1|0.9|Sarsa max|
|9.26|0.75|0.15|0.9|Sarsa max|
|9.26|0.6|0.2|0.9|Sarsa expected|
|9.26|0.6|0.2|0.85|Sarsa max|
|9.25|0.9|0.05|1.0|Sarsa expected|
|9.25|0.45|0.05|1.0|Sarsa max|
|9.25|0.75|0.05|0.9|Sarsa expected|
|9.25|0.45|0.1|0.85|Sarsa expected|
|9.25|0.6|0.15|0.95|Sarsa max|
|9.25|0.75|0.15|0.85|Sarsa expected|
|9.25|0.6|0.2|1.0|Sarsa expected|
|9.25|0.75|0.2|0.95|Sarsa max|
|9.25|0.6|0.2|0.9|Sarsa max|
|9.25|0.75|0.2|0.85|Sarsa expected|
|9.24|0.75|0.05|1.0|Sarsa expected|
|9.24|0.9|0.05|0.95|Sarsa expected|
|9.24|0.45|0.1|1.0|Sarsa expected|
|9.24|0.9|0.15|0.85|Sarsa expected|
|9.23|0.9|0.05|0.95|Sarsa max|
|9.23|0.9|0.05|0.85|Sarsa max|
|9.23|0.9|0.1|0.85|Sarsa expected|
|9.23|0.75|0.15|0.95|Sarsa max|
|9.23|0.9|0.2|0.85|Sarsa max|
|9.22|0.6|0.05|0.85|Sarsa expected|
|9.22|0.75|0.1|0.95|Sarsa expected|
|9.22|0.45|0.1|0.95|Sarsa max|
|9.22|0.45|0.2|1.0|Sarsa expected|
|9.22|0.45|0.2|0.9|Sarsa expected|
|9.22|0.9|0.2|0.85|Sarsa expected|
|9.22|0.75|0.2|0.85|Sarsa max|
|9.21|0.6|0.05|1.0|Sarsa expected|
|9.21|0.9|0.05|0.9|Sarsa expected|
|9.21|0.9|0.1|1.0|Sarsa max|
|9.21|0.6|0.1|1.0|Sarsa expected|
|9.21|0.45|0.1|1.0|Sarsa max|
|9.21|0.75|0.15|1.0|Sarsa max|
|9.21|0.45|0.15|1.0|Sarsa max|
|9.21|0.75|0.15|0.85|Sarsa max|
|9.2|0.75|0.05|1.0|Sarsa max|
|9.19|0.45|0.1|0.9|Sarsa max|
|9.19|0.9|0.15|1.0|Sarsa expected|
|9.19|0.6|0.15|1.0|Sarsa max|
|9.19|0.45|0.15|1.0|Sarsa expected|
|9.19|0.75|0.15|0.9|Sarsa expected|
|9.19|0.9|0.2|0.9|Sarsa max|
|9.19|0.9|0.2|0.9|Sarsa expected|
|9.18|0.9|0.1|1.0|Sarsa expected|
|9.18|0.75|0.2|1.0|Sarsa max|
|9.17|0.6|0.15|1.0|Sarsa expected|
|9.17|0.6|0.2|0.95|Sarsa max|
|9.16|0.9|0.05|1.0|Sarsa max|
|9.16|0.75|0.05|0.95|Sarsa max|
|9.16|0.6|0.1|0.95|Sarsa expected|
|9.15|0.45|0.05|0.85|Sarsa max|
|9.15|0.75|0.1|0.85|Sarsa max|
|9.15|0.9|0.2|0.95|Sarsa max|
|9.15|0.45|0.2|0.9|Sarsa max|
|9.14|0.9|0.2|1.0|Sarsa max|
|9.12|0.6|0.15|0.95|Sarsa expected|
|9.09|0.9|0.15|0.95|Sarsa expected|
|9.09|0.45|0.2|0.95|Sarsa expected|

## Output
```
Epsilon change=0.6, Alpha=0.2, Gamma=0.85, Type=Sarsa max
Episode 20000/20000 || Best average reward 9.26  , current average reward 8.96

Total avg rewards= 5.668

Start
+---------+
|R: | : :G|
| : : : : |
| : : : : |
| | : | : |
|Y| : |B: |
+---------+


Iteration 15, Cumaltive reward 6
+---------+
|R: | : :G|
| : : : : |
| : : : : |
| | : | : |
|Y| : |B: |
+---------+
  (Dropoff)

Final reward=6

Episode 100000/100000 || Best average reward 9.37  , current average reward 8.47

Total avg rewards= 8.44849
Top 5 configuration so far
Best average reward=9.59, Epsilon change=0.45, Alpha=0.05, Gamma=0.85, Type=Sarsa expected
Best average reward=9.56, Epsilon change=0.75, Alpha=0.1, Gamma=0.9, Type=Sarsa expected
Best average reward=9.52, Epsilon change=0.45, Alpha=0.05, Gamma=0.95, Type=Sarsa expected
Best average reward=9.51, Epsilon change=0.75, Alpha=0.15, Gamma=0.95, Type=Sarsa expected
Best average reward=9.46, Epsilon change=0.6, Alpha=0.2, Gamma=0.95, Type=Sarsa expected

Epsilon change=0.6, Alpha=0.2, Gamma=0.85, Type=Sarsa expected
Episode 20000/20000 || Best average reward 9.28  , current average reward 8.12

Total avg rewards= 5.5344

Start
+---------+
|R: | : :G|
| : : : : |
| : : : : |
| | : | : |
|Y| : |B: |
+---------+


Iteration 16, Cumaltive reward 5
+---------+
|R: | : :G|
| : : : : |
| : : : : |
| | : | : |
|Y| : |B: |
+---------+
  (Dropoff)

Final reward=5

Episode 100000/100000 || Best average reward 9.48  , current average reward 8.53

Total avg rewards= 8.28445
Top 5 configuration so far
Best average reward=9.59, Epsilon change=0.45, Alpha=0.05, Gamma=0.85, Type=Sarsa expected
Best average reward=9.56, Epsilon change=0.75, Alpha=0.1, Gamma=0.9, Type=Sarsa expected
Best average reward=9.52, Epsilon change=0.45, Alpha=0.05, Gamma=0.95, Type=Sarsa expected
Best average reward=9.51, Epsilon change=0.75, Alpha=0.15, Gamma=0.95, Type=Sarsa expected
Best average reward=9.46, Epsilon change=0.6, Alpha=0.2, Gamma=0.95, Type=Sarsa expected

Epsilon change=0.45, Alpha=0.2, Gamma=0.85, Type=Sarsa max
Episode 20000/20000 || Best average reward 9.28  , current average reward 8.45

Total avg rewards= 5.72345

Start
+---------+
|R: | : :G|
| : : : : |
| : : : : |
| | : | : |
|Y| : |B: |
+---------+


Iteration 16, Cumaltive reward 5
+---------+
|R: | : :G|
| : : : : |
| : : : : |
| | : | : |
|Y| : |B: |
+---------+
  (Dropoff)

Final reward=5

Episode 100000/100000 || Best average reward 9.59  , current average reward 8.67

Total avg rewards= 8.46225
Top 5 configuration so far
Best average reward=9.59, Epsilon change=0.45, Alpha=0.05, Gamma=0.85, Type=Sarsa expected
Best average reward=9.56, Epsilon change=0.75, Alpha=0.1, Gamma=0.9, Type=Sarsa expected
Best average reward=9.52, Epsilon change=0.45, Alpha=0.05, Gamma=0.95, Type=Sarsa expected
Best average reward=9.51, Epsilon change=0.75, Alpha=0.15, Gamma=0.95, Type=Sarsa expected
Best average reward=9.46, Epsilon change=0.6, Alpha=0.2, Gamma=0.95, Type=Sarsa expected

Epsilon change=0.45, Alpha=0.2, Gamma=0.85, Type=Sarsa expected
Episode 20000/20000 || Best average reward 9.29  , current average reward 9.12

Total avg rewards= 5.73365

Start
+---------+
|R: | : :G|
| : : : : |
| : : : : |
| | : | : |
|Y| : |B: |
+---------+


Iteration 12, Cumaltive reward 9
+---------+
|R: | : :G|
| : : : : |
| : : : : |
| | : | : |
|Y| : |B: |
+---------+
  (Dropoff)

Final reward=9

Episode 100000/100000 || Best average reward 9.41  , current average reward 8.46

Total avg rewards= 8.44969
Top 5 configuration so far
Best average reward=9.59, Epsilon change=0.45, Alpha=0.05, Gamma=0.85, Type=Sarsa expected
Best average reward=9.56, Epsilon change=0.75, Alpha=0.1, Gamma=0.9, Type=Sarsa expected
Best average reward=9.52, Epsilon change=0.45, Alpha=0.05, Gamma=0.95, Type=Sarsa expected
Best average reward=9.51, Epsilon change=0.75, Alpha=0.15, Gamma=0.95, Type=Sarsa expected
Best average reward=9.46, Epsilon change=0.6, Alpha=0.2, Gamma=0.95, Type=Sarsa expected

Completed for
Alphas=[0.05, 0.1, 0.15, 0.2]
Gammas=[1.0, 0.95, 0.9, 0.85]
Epsilon change=[0.9, 0.75, 0.6, 0.45]
Type=['max', 'expected']

Results
Best average reward=9.59, Epsilon change=0.45, Alpha=0.05, Gamma=0.85, Type=Sarsa expected
Best average reward=9.56, Epsilon change=0.75, Alpha=0.1, Gamma=0.9, Type=Sarsa expected
Best average reward=9.52, Epsilon change=0.45, Alpha=0.05, Gamma=0.95, Type=Sarsa expected
Best average reward=9.51, Epsilon change=0.75, Alpha=0.15, Gamma=0.95, Type=Sarsa expected
Best average reward=9.46, Epsilon change=0.6, Alpha=0.2, Gamma=0.95, Type=Sarsa expected
Best average reward=9.44, Epsilon change=0.75, Alpha=0.1, Gamma=1.0, Type=Sarsa max
Best average reward=9.44, Epsilon change=0.6, Alpha=0.1, Gamma=0.9, Type=Sarsa expected
Best average reward=9.41, Epsilon change=0.9, Alpha=0.2, Gamma=1.0, Type=Sarsa expected
Best average reward=9.4, Epsilon change=0.75, Alpha=0.1, Gamma=0.95, Type=Sarsa max
Best average reward=9.39, Epsilon change=0.75, Alpha=0.05, Gamma=0.85, Type=Sarsa max
Best average reward=9.39, Epsilon change=0.9, Alpha=0.15, Gamma=1.0, Type=Sarsa max
Best average reward=9.39, Epsilon change=0.45, Alpha=0.2, Gamma=0.95, Type=Sarsa max
Best average reward=9.39, Epsilon change=0.75, Alpha=0.2, Gamma=0.9, Type=Sarsa max
Best average reward=9.38, Epsilon change=0.9, Alpha=0.05, Gamma=0.9, Type=Sarsa max
Best average reward=9.37, Epsilon change=0.75, Alpha=0.1, Gamma=1.0, Type=Sarsa expected
Best average reward=9.37, Epsilon change=0.6, Alpha=0.1, Gamma=0.9, Type=Sarsa max
Best average reward=9.37, Epsilon change=0.75, Alpha=0.1, Gamma=0.85, Type=Sarsa expected
Best average reward=9.37, Epsilon change=0.45, Alpha=0.1, Gamma=0.85, Type=Sarsa max
Best average reward=9.36, Epsilon change=0.6, Alpha=0.05, Gamma=0.95, Type=Sarsa max
Best average reward=9.36, Epsilon change=0.9, Alpha=0.05, Gamma=0.85, Type=Sarsa expected
Best average reward=9.36, Epsilon change=0.6, Alpha=0.1, Gamma=1.0, Type=Sarsa max
Best average reward=9.36, Epsilon change=0.9, Alpha=0.15, Gamma=0.9, Type=Sarsa max
Best average reward=9.36, Epsilon change=0.6, Alpha=0.15, Gamma=0.9, Type=Sarsa max
Best average reward=9.34, Epsilon change=0.75, Alpha=0.05, Gamma=0.95, Type=Sarsa expected
Best average reward=9.34, Epsilon change=0.6, Alpha=0.05, Gamma=0.9, Type=Sarsa max
Best average reward=9.34, Epsilon change=0.9, Alpha=0.1, Gamma=0.9, Type=Sarsa expected
Best average reward=9.34, Epsilon change=0.45, Alpha=0.1, Gamma=0.9, Type=Sarsa expected
Best average reward=9.34, Epsilon change=0.6, Alpha=0.15, Gamma=0.85, Type=Sarsa expected
Best average reward=9.33, Epsilon change=0.45, Alpha=0.1, Gamma=0.95, Type=Sarsa expected
Best average reward=9.33, Epsilon change=0.45, Alpha=0.15, Gamma=0.9, Type=Sarsa max
Best average reward=9.32, Epsilon change=0.6, Alpha=0.05, Gamma=1.0, Type=Sarsa max
Best average reward=9.32, Epsilon change=0.45, Alpha=0.05, Gamma=1.0, Type=Sarsa expected
Best average reward=9.32, Epsilon change=0.9, Alpha=0.15, Gamma=0.9, Type=Sarsa expected
Best average reward=9.32, Epsilon change=0.9, Alpha=0.15, Gamma=0.85, Type=Sarsa max
Best average reward=9.31, Epsilon change=0.6, Alpha=0.05, Gamma=0.85, Type=Sarsa max
Best average reward=9.31, Epsilon change=0.9, Alpha=0.1, Gamma=0.95, Type=Sarsa max
Best average reward=9.31, Epsilon change=0.9, Alpha=0.1, Gamma=0.95, Type=Sarsa expected
Best average reward=9.31, Epsilon change=0.6, Alpha=0.1, Gamma=0.85, Type=Sarsa expected
Best average reward=9.31, Epsilon change=0.6, Alpha=0.15, Gamma=0.85, Type=Sarsa max
Best average reward=9.31, Epsilon change=0.75, Alpha=0.2, Gamma=0.9, Type=Sarsa expected
Best average reward=9.3, Epsilon change=0.6, Alpha=0.1, Gamma=0.95, Type=Sarsa max
Best average reward=9.3, Epsilon change=0.45, Alpha=0.15, Gamma=0.95, Type=Sarsa expected
Best average reward=9.29, Epsilon change=0.6, Alpha=0.05, Gamma=0.95, Type=Sarsa expected
Best average reward=9.29, Epsilon change=0.6, Alpha=0.05, Gamma=0.9, Type=Sarsa expected
Best average reward=9.29, Epsilon change=0.75, Alpha=0.05, Gamma=0.85, Type=Sarsa expected
Best average reward=9.29, Epsilon change=0.9, Alpha=0.15, Gamma=0.95, Type=Sarsa max
Best average reward=9.29, Epsilon change=0.45, Alpha=0.15, Gamma=0.95, Type=Sarsa max
Best average reward=9.29, Epsilon change=0.45, Alpha=0.15, Gamma=0.9, Type=Sarsa expected
Best average reward=9.29, Epsilon change=0.45, Alpha=0.2, Gamma=1.0, Type=Sarsa max
Best average reward=9.29, Epsilon change=0.45, Alpha=0.2, Gamma=0.85, Type=Sarsa expected
Best average reward=9.28, Epsilon change=0.45, Alpha=0.05, Gamma=0.9, Type=Sarsa expected
Best average reward=9.28, Epsilon change=0.75, Alpha=0.1, Gamma=0.9, Type=Sarsa max
Best average reward=9.28, Epsilon change=0.9, Alpha=0.1, Gamma=0.85, Type=Sarsa max
Best average reward=9.28, Epsilon change=0.6, Alpha=0.1, Gamma=0.85, Type=Sarsa max
Best average reward=9.28, Epsilon change=0.75, Alpha=0.15, Gamma=1.0, Type=Sarsa expected
Best average reward=9.28, Epsilon change=0.45, Alpha=0.15, Gamma=0.85, Type=Sarsa expected
Best average reward=9.28, Epsilon change=0.9, Alpha=0.2, Gamma=0.95, Type=Sarsa expected
Best average reward=9.28, Epsilon change=0.75, Alpha=0.2, Gamma=0.95, Type=Sarsa expected
Best average reward=9.28, Epsilon change=0.6, Alpha=0.2, Gamma=0.85, Type=Sarsa expected
Best average reward=9.28, Epsilon change=0.45, Alpha=0.2, Gamma=0.85, Type=Sarsa max
Best average reward=9.27, Epsilon change=0.75, Alpha=0.05, Gamma=0.9, Type=Sarsa max
Best average reward=9.27, Epsilon change=0.45, Alpha=0.05, Gamma=0.9, Type=Sarsa max
Best average reward=9.27, Epsilon change=0.6, Alpha=0.15, Gamma=0.9, Type=Sarsa expected
Best average reward=9.27, Epsilon change=0.45, Alpha=0.15, Gamma=0.85, Type=Sarsa max
Best average reward=9.27, Epsilon change=0.75, Alpha=0.2, Gamma=1.0, Type=Sarsa expected
Best average reward=9.27, Epsilon change=0.6, Alpha=0.2, Gamma=1.0, Type=Sarsa max
Best average reward=9.26, Epsilon change=0.45, Alpha=0.05, Gamma=0.95, Type=Sarsa max
Best average reward=9.26, Epsilon change=0.9, Alpha=0.1, Gamma=0.9, Type=Sarsa max
Best average reward=9.26, Epsilon change=0.75, Alpha=0.15, Gamma=0.9, Type=Sarsa max
Best average reward=9.26, Epsilon change=0.6, Alpha=0.2, Gamma=0.9, Type=Sarsa expected
Best average reward=9.26, Epsilon change=0.6, Alpha=0.2, Gamma=0.85, Type=Sarsa max
Best average reward=9.25, Epsilon change=0.9, Alpha=0.05, Gamma=1.0, Type=Sarsa expected
Best average reward=9.25, Epsilon change=0.45, Alpha=0.05, Gamma=1.0, Type=Sarsa max
Best average reward=9.25, Epsilon change=0.75, Alpha=0.05, Gamma=0.9, Type=Sarsa expected
Best average reward=9.25, Epsilon change=0.45, Alpha=0.1, Gamma=0.85, Type=Sarsa expected
Best average reward=9.25, Epsilon change=0.6, Alpha=0.15, Gamma=0.95, Type=Sarsa max
Best average reward=9.25, Epsilon change=0.75, Alpha=0.15, Gamma=0.85, Type=Sarsa expected
Best average reward=9.25, Epsilon change=0.6, Alpha=0.2, Gamma=1.0, Type=Sarsa expected
Best average reward=9.25, Epsilon change=0.75, Alpha=0.2, Gamma=0.95, Type=Sarsa max
Best average reward=9.25, Epsilon change=0.6, Alpha=0.2, Gamma=0.9, Type=Sarsa max
Best average reward=9.25, Epsilon change=0.75, Alpha=0.2, Gamma=0.85, Type=Sarsa expected
Best average reward=9.24, Epsilon change=0.75, Alpha=0.05, Gamma=1.0, Type=Sarsa expected
Best average reward=9.24, Epsilon change=0.9, Alpha=0.05, Gamma=0.95, Type=Sarsa expected
Best average reward=9.24, Epsilon change=0.45, Alpha=0.1, Gamma=1.0, Type=Sarsa expected
Best average reward=9.24, Epsilon change=0.9, Alpha=0.15, Gamma=0.85, Type=Sarsa expected
Best average reward=9.23, Epsilon change=0.9, Alpha=0.05, Gamma=0.95, Type=Sarsa max
Best average reward=9.23, Epsilon change=0.9, Alpha=0.05, Gamma=0.85, Type=Sarsa max
Best average reward=9.23, Epsilon change=0.9, Alpha=0.1, Gamma=0.85, Type=Sarsa expected
Best average reward=9.23, Epsilon change=0.75, Alpha=0.15, Gamma=0.95, Type=Sarsa max
Best average reward=9.23, Epsilon change=0.9, Alpha=0.2, Gamma=0.85, Type=Sarsa max
Best average reward=9.22, Epsilon change=0.6, Alpha=0.05, Gamma=0.85, Type=Sarsa expected
Best average reward=9.22, Epsilon change=0.75, Alpha=0.1, Gamma=0.95, Type=Sarsa expected
Best average reward=9.22, Epsilon change=0.45, Alpha=0.1, Gamma=0.95, Type=Sarsa max
Best average reward=9.22, Epsilon change=0.45, Alpha=0.2, Gamma=1.0, Type=Sarsa expected
Best average reward=9.22, Epsilon change=0.45, Alpha=0.2, Gamma=0.9, Type=Sarsa expected
Best average reward=9.22, Epsilon change=0.9, Alpha=0.2, Gamma=0.85, Type=Sarsa expected
Best average reward=9.22, Epsilon change=0.75, Alpha=0.2, Gamma=0.85, Type=Sarsa max
Best average reward=9.21, Epsilon change=0.6, Alpha=0.05, Gamma=1.0, Type=Sarsa expected
Best average reward=9.21, Epsilon change=0.9, Alpha=0.05, Gamma=0.9, Type=Sarsa expected
Best average reward=9.21, Epsilon change=0.9, Alpha=0.1, Gamma=1.0, Type=Sarsa max
Best average reward=9.21, Epsilon change=0.6, Alpha=0.1, Gamma=1.0, Type=Sarsa expected
Best average reward=9.21, Epsilon change=0.45, Alpha=0.1, Gamma=1.0, Type=Sarsa max
Best average reward=9.21, Epsilon change=0.75, Alpha=0.15, Gamma=1.0, Type=Sarsa max
Best average reward=9.21, Epsilon change=0.45, Alpha=0.15, Gamma=1.0, Type=Sarsa max
Best average reward=9.21, Epsilon change=0.75, Alpha=0.15, Gamma=0.85, Type=Sarsa max
Best average reward=9.2, Epsilon change=0.75, Alpha=0.05, Gamma=1.0, Type=Sarsa max
Best average reward=9.19, Epsilon change=0.45, Alpha=0.1, Gamma=0.9, Type=Sarsa max
Best average reward=9.19, Epsilon change=0.9, Alpha=0.15, Gamma=1.0, Type=Sarsa expected
Best average reward=9.19, Epsilon change=0.6, Alpha=0.15, Gamma=1.0, Type=Sarsa max
Best average reward=9.19, Epsilon change=0.45, Alpha=0.15, Gamma=1.0, Type=Sarsa expected
Best average reward=9.19, Epsilon change=0.75, Alpha=0.15, Gamma=0.9, Type=Sarsa expected
Best average reward=9.19, Epsilon change=0.9, Alpha=0.2, Gamma=0.9, Type=Sarsa max
Best average reward=9.19, Epsilon change=0.9, Alpha=0.2, Gamma=0.9, Type=Sarsa expected
Best average reward=9.18, Epsilon change=0.9, Alpha=0.1, Gamma=1.0, Type=Sarsa expected
Best average reward=9.18, Epsilon change=0.75, Alpha=0.2, Gamma=1.0, Type=Sarsa max
Best average reward=9.17, Epsilon change=0.6, Alpha=0.15, Gamma=1.0, Type=Sarsa expected
Best average reward=9.17, Epsilon change=0.6, Alpha=0.2, Gamma=0.95, Type=Sarsa max
Best average reward=9.16, Epsilon change=0.9, Alpha=0.05, Gamma=1.0, Type=Sarsa max
Best average reward=9.16, Epsilon change=0.75, Alpha=0.05, Gamma=0.95, Type=Sarsa max
Best average reward=9.16, Epsilon change=0.6, Alpha=0.1, Gamma=0.95, Type=Sarsa expected
Best average reward=9.15, Epsilon change=0.45, Alpha=0.05, Gamma=0.85, Type=Sarsa max
Best average reward=9.15, Epsilon change=0.75, Alpha=0.1, Gamma=0.85, Type=Sarsa max
Best average reward=9.15, Epsilon change=0.9, Alpha=0.2, Gamma=0.95, Type=Sarsa max
Best average reward=9.15, Epsilon change=0.45, Alpha=0.2, Gamma=0.9, Type=Sarsa max
Best average reward=9.14, Epsilon change=0.9, Alpha=0.2, Gamma=1.0, Type=Sarsa max
Best average reward=9.12, Epsilon change=0.6, Alpha=0.15, Gamma=0.95, Type=Sarsa expected
Best average reward=9.09, Epsilon change=0.9, Alpha=0.15, Gamma=0.95, Type=Sarsa expected
Best average reward=9.09, Epsilon change=0.45, Alpha=0.2, Gamma=0.95, Type=Sarsa expected



```