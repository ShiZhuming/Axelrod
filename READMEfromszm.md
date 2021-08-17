# 工作概况

## 如何修改不对称？

在axelrod/game.py中修改class Game(object)中的__init__，里面是支付矩阵

## 库中间有哪些策略？

strategies.txt中列出了，也可以用print(axl.strategies)列出

## memory-one的有哪些？

<class 'axelrod.strategies.memoryone.ALLCorALLD'>类似这样列出，但没有归类为memoryone的策略里有没有memoryone的我还不知道，看起来有memory_depth这个属性

## 碰到的问题？

变成不对称后，待排列的东西变成了一个pair（A，B），而且老师要求增加一个维度：第一轮的策略