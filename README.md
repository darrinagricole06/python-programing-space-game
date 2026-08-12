# Space Explorer

Welcome aboard. Over nine sessions, you will turn this starter game into your own space adventure while learning Python.

The game already works. At first, some code will be a black box. You will understand and replace more of it each week.

## What you need

- [VS Code](https://code.visualstudio.com/download?_exp_download=d53503e735) 
- [Git](https://git-scm.com/install/)
- [uv](https://docs.astral.sh/uv/)
- [A GitHub account](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://github.com/login&ved=2ahUKEwin1aC_opqWAxUs8LsIHXeHKgUQFnoECCIQAQ&usg=AOvVaw0YPQjBCLvq4nLugtBaJju7)

Your instructor (me) will help you install and check these tools.

## Get the project

```bash
git clone https://github.com/ocean-ai-seychelles/young-innovators-challenge.git
cd space-explorer-starter
```

## Run the game

```bash
uv run game.py
```

The first run may take a little longer while uv prepares Python. The starter game flies automatically; you will add player controls in Session 2.

## Session 1

Open `constants.py`. Change your ship name, crew description, starting oxygen, starting hull, and galaxy size. Run the game after each change.

Save your work:

```bash
git add constants.py
git commit -m "session 1: personalised my ship"
git push
```

## Project map

```text
constants.py    Your ship and game settings
game.py         The main program
engine/         Supplied game machinery, revealed over time
```

Do not worry if the engine looks unfamiliar. That is intentional. By the final session, you will understand how the whole game fits together.
