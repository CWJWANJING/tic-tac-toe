# tic-tac-toe


This game is the classic tic-tac-toe game, which players each place a notion, either **X** or **O** in a 井 shape squares:


<pre>
     1   2   3
  a  O |   | X
    -----------
  b    | O |
    -----------
  c    |   |
</pre>

Players need to type in the co-ordinates of the blank space in the form of ***a1***, ***a2***, and etc.. The left column a, b, c and the top row 1, 2, 3 are for instructing players to enter the valid co-ordinates. This version can be played between two devices on local network. 

# To play
The server side is the **X**, and needs to run command:

```python
python tic-tac-toe.py server
```

The client side is the **O**, and needs to run command:

```python
python tic-tac-toe.py ***enter this machine's ip address***
```

Here is a video how it is played:

![Demo](tttdemo_small.mp4)

