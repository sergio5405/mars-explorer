# mars-explorer
School assignment - Multi Agent System collecting stuff on Mars

## Run me

```bash
python main.py --help
usage: main.py [-h] [--obstacles OBSTACLES] [--rocks ROCKS]
               [--explorers EXPLORERS] [--collaborative]

optional arguments:
  -h, --help            show this help message and exit
  --obstacles OBSTACLES
  --rocks ROCKS
  --explorers EXPLORERS
  --collaborative [OPTIONAL]

```

All params have defaults.

## Details

### Explorers

* can carry 1 rock
* know where the base is
* can sense nearby rocks
* can sense if they are "on" a rock or the base

### Carriers

* can carry any number of rocks
* can go to an explorer agent


## Modes

### Individual

![demo-without-carriers](https://raw.githubusercontent.com/mihneadb/mars-explorer/master/demo-gifs/mars-explorer-no-carriers.gif)

### Collaborative

Explorers wander about. When they find a rock, they stop, and drop a crumb. When other explorer
meets the crumb, it will pick it up and try to follow the path to find more rocks.

```
--collaborative
```

![demo-with-carriers](https://raw.githubusercontent.com/mihneadb/mars-explorer/master/demo-gifs/mars-explorer-carriers.gif)
