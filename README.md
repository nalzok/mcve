# PyCharm "Optimized Imports" bug MCVE

Run `Optimized Imports` on this project and watch it fail.


### Quick Analysis

PyCharm optimizes that import statements by sorting them in lexicographical order. Thus, the following statements in `cmds.py`

```
from app.stuff.models import Stuff
from app.business_logic import update_stuff
```

get reordered as

```
from app.business_logic import update_stuff
from app.stuff.models import Stuff
```

which causes a circular import.


### Version Information

```
PyCharm 2020.2 (Professional Edition)
Build #PY-202.6397.98, built on July 27, 2020
Licensed to sun qingyao
Subscription is active until February 4, 2021
For educational use only.
Runtime version: 11.0.7+10-b944.20 amd64
VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o.
Windows 10 10.0
GC: ParNew, ConcurrentMarkSweep
Memory: 976M
Cores: 6
Non-Bundled Plugins: IdeaVIM, com.jetbrains.hackathon2015.S, name.kropp.intellij.makefile, net.vektah.codeglance, com.jetbrains.intellij.datalore, ru.meanmail.plugin.requirements
```