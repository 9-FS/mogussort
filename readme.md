---
Topic: "Mogussort"
Author: "구FS"
---
<link href="./doc_templates/md_style.css" rel="stylesheet"></link>
<body>

# <p style="text-align: center">Mogussort</p>
<br>
<br>

<div class="img_right_30">
    <img alt="Error: Could not load image source."
    src="https://media.tenor.com/1iSARWJr-TEAAAAC/among-us-twerk.gif"/>
    <p class=img_caption>😤😩😩💦💦💦</p>
</div>

- [1. 📮Mogussort](#1-mogussort)
- [2. 📮Lore📮](#2-lore)
- [3. Installation](#3-installation)
- [4. 📮How it works📮](#4-how-it-works)
- [5. 📮Performance📮](#5-performance)
- [6. 📮Sus📮](#6-sus)
- [7. Language](#7-language)

## 1. 📮Mogussort

World's (📮)SUSSIEST sorting algorithm

## 2. 📮Lore📮

<div class="img_right_30">
    <img alt="Error: Could not load image source."
    src="https://i.imgflip.com/5y6poi.jpg"/>
    <p class=img_caption>sussy</p>
</div>

Your normal and boring sorting algorithms are just too fast? You want to introduce some sussy code to your programs?  
Then you have come to the right place.

Inspired by the fantastic [Csussus version](https://github.com/sam-k0/Mogussort/) and certified 📮extra sussy📮 by the original author!

## 3. Installation

You can install 📮Mogussort📮 from PyPi with `pip install Mogussort`.

<div style="page-break-after: always;"></div>

## 4. 📮How it works📮

There are 2 (two, 2📮) lists, `crew_in` and `crew_out`.

- `crew_in` contains all crewmates at the start of the game.
- `crew_out` is empty.

The algorithm will vote out one random crewmate and put it in `crew_out` That crewmate is then removed from `crew_in`. Then, it checks if `crew_out` is correctly sorted (ascending).

If it is correnct, it will continue to vote and populate `crew_out`.

If the crewmates are not in the right order an 📮Impostor📮 (sus, baka) has been spotted. This means that the game is lost, and `crew_out` will be cleared, and `crew_in` will be reset to the original form.

The algorithm will stop once all crewmates are in the right order.

<div style="page-break-after: always;"></div>

## 5. 📮Performance📮

<div class="img_right_30">
    <img alt="Error: Could not load image source."
    src="https://repository-images.githubusercontent.com/468220029/dfe7cf55-8b30-4c65-8e9f-b2245b9e8bcb"/>
    <p class=img_caption></p>
</div>

The 📮mogussort solves all of your sorting problems with an incredible, luck based runtime. You might ask "how fast is it exactly?".

Well, having $c$ crew mates the probability $p$ of ~~sorting~~ voting correctly in $1$ ~~attempts to sort~~ emergency meeting is:

$$
\begin{align}
p&=\frac{1}{c} \cdot \frac{1}{c-1} \cdot \frac{1}{c-2} \cdot ... \cdot \frac{1}{1} \\
&=\frac{1}{c!}
\end{align}
$$

That means the probability to fail in $1$ emergency meeting is:

$$
\begin{align}
1-p=1- \frac{1}{c!}
\end{align}
$$

If we make $n$ emergency meetings, the chance $P$ of $1$ success is:

$$
\begin{align}
P&=1-(1-p)^{n} \\
&=1-(1- \frac{1}{c!})^{n}
\end{align}
$$

So, how many meetings do we need until we have a chance of $P$ to have them sorted correctly once?

$$
\begin{align}
P &= 1-(1- \frac{1}{c!})^{n}\\
(1- \frac{1}{c!})^{n} &= 1-P \\
n &= \text{log}_{1- \frac{1}{c!}}(1-P) \\
n &= \frac{\text{lg}(1-P)}{\text{lg}(1- \frac{1}{c!})}
\end{align}
$$

So if we manage $m$ meetings per second, mogussort will finish with a probability $P$ within time $t_{P}$:

$$
\begin{align}
t_{P} &= \frac{n}{m} \\
&= \frac{\text{lg}(1-P)}{\text{lg}(1- \frac{1}{c!})} \cdot \frac{1}{m}
\end{align}
$$

<div style="page-break-after: always;"></div>

Let's assume we manage $m=60 \text{k} \frac{\text{meeting}}{\text{s}}$ , which is a value I roughly get on my computer (Intel Core i7-8550U). Then mogussort will finish with a probability $P$ of $0,50$ and $0,95$ within:

<div align="center">

| Crew Mates $c$ |   Time $t_{0,50}$ |    Time $t_{0,50}$ |   Time $t_{0,95}$ |     Time $t_{0,95}$ |
| -------------: | ----------------: | -----------------: | ----------------: | ------------------: |
|            $2$ | $16,67 \text{µs}$ |                    | $72,03 \text{µs}$ |
|            $3$ | $63,36 \text{µs}$ |                    | $273,9 \text{µs}$ |
|            $4$ | $271,4 \text{µs}$ |                    | $1,173 \text{ms}$ |
|            $5$ | $1,381 \text{ms}$ |                    | $5,966 \text{ms}$ |
|            $6$ | $8,312 \text{ms}$ |                    | $35,92 \text{ms}$ |
|            $7$ | $58,22 \text{ms}$ |                    | $251,6 \text{ms}$ |
|            $8$ | $465,8 \text{ms}$ |                    |  $2,013 \text{s}$ |
|            $9$ |  $4,192 \text{s}$ |                    |  $18,12 \text{s}$ |
|           $10$ |  $41,92 \text{s}$ |                    |  $181,2 \text{s}$ |  $(3,0 \text{min})$ |
|           $11$ |  $461,1 \text{s}$ | $(7,7 \text{min})$ | $1,993 \text{ks}$ |   $(33 \text{min})$ |
|           $12$ | $5,534 \text{ks}$ |   $(1,5 \text{h})$ | $23,92 \text{ks}$ |    $(6,6 \text{h})$ |
|           $13$ | $71,94 \text{ks}$ |    $(20 \text{h})$ | $310,9 \text{ks}$ |    $(3,6 \text{d})$ |
|           $14$ | $1,007 \text{Ms}$ |    $(12 \text{d})$ | $4,353 \text{Ms}$ |     $(50 \text{d})$ |
|           $15$ | $15,11 \text{Ms}$ |   $(170 \text{d})$ | $65,29 \text{Ms}$ |    $(2,1 \text{a})$ |
|           $16$ | $242,0 \text{Ms}$ |   $(7,7 \text{a})$ | $1,046 \text{Gs}$ |     $(33 \text{a})$ |
|           $17$ | $4,162 \text{Gs}$ |   $(132 \text{a})$ | $17,99 \text{Gs}$ |    $(570 \text{a})$ |
|           $18$ | $104,1 \text{Gs}$ | $(3.297 \text{a})$ | $449,7 \text{Gs}$ | $(14.251 \text{a})$ |

</div>

This even means you might be able to play a game of Among Us while you wait for the algorithm to finish (now isn't that fantastic?).

<div style="page-break-after: always;"></div>

## 6. 📮Sus📮

```python
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⣀⣀⣐⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⢠⠄⣠⣶⣿⣿⣿⠿⠿⣛⣂⣀⣀⡒⠶⣶⣤⣤⣬⣀⡀⠄⢀⠄⠄⠄⠄⠄⠄⠄
⠄⠄⢀⣾⣿⣿⣿⡟⢡⢾⣿⣿⣿⣿⣿⣿⣶⣌⠻⣿⣿⣿⣿⣷⣦⣄⡀⠄⠄⠄⠄⠄
⠄⠄⣈⣉⡛⣿⣿⣿⡌⢇⢻⣿⣿⣿⣿⣿⠿⠛⣡⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠄⠄⠄
⠄⠺⠟⣉⣴⡿⠛⣩⣾⣎⠳⠿⠛⣋⣩⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠄⠄
⠄⠄⠄⠘⢋⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄
⠄⠄⢀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄
⠄⠄⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣀
⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠘⠛
⠄⠄⠄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⣀⣀⣠⣤
⠄⠄⣀⣀⡙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢛⣩⠤⠾⠄⠛⠋⠉⢉
⠄⠺⠿⠛⠛⠃⠄⠉⠙⠛⠛⠻⠿⠿⠿⠟⠛⠛⠛⠉⠁⠄⠄⣀⣀⣠⣤⣠⣴⣶⣼⣿
```

```python
⠀⠀⠀⡯⡯⡾⠝⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢊⠘⡮⣣⠪⠢⡑⡌ 
⠀⠀⠟⠝⠈⠀⠀⠀⠡⠀⠠⢈⠠⢐⢠⢂⢔⣐⢄⡂⢔⠀⡁⢉⠸⢨⢑⠕⡌
⠀⠀⡀⠁⠀⠀⠀⡀⢂⠡⠈⡔⣕⢮⣳⢯⣿⣻⣟⣯⣯⢷⣫⣆⡂⠀⠀⢐⠑⡌ 
⢀⠠⠐⠈⠀⢀⢂⠢⡂⠕⡁⣝⢮⣳⢽⡽⣾⣻⣿⣯⡯⣟⣞⢾⢜⢆⠀⡀⠀⠪
⣬⠂⠀⠀⢀⢂⢪⠨⢂⠥⣺⡪⣗⢗⣽⢽⡯⣿⣽⣷⢿⡽⡾⡽⣝⢎⠀⠀⠀⢡ 
⣿⠀⠀⠀⢂⠢⢂⢥⢱⡹⣪⢞⡵⣻⡪⡯⡯⣟⡾⣿⣻⡽⣯⡻⣪⠧⠑⠀⠁⢐
⣿⠀⠀⠀⠢⢑⠠⠑⠕⡝⡎⡗⡝⡎⣞⢽⡹⣕⢯⢻⠹⡹⢚⠝⡷⡽⡨⠀⠀⢔ 
⣿⡯⠀⢈⠈⢄⠂⠂⠐⠀⠌⠠⢑⠱⡱⡱⡑⢔⠁⠀⡀⠐⠐⠐⡡⡹⣪⠀⠀⢘
⣿⣽⠀⡀⡊⠀⠐⠨⠈⡁⠂⢈⠠⡱⡽⣷⡑⠁⠠⠑⠀⢉⢇⣤⢘⣪⢽⠀⢌⢎
⣿⢾⠀⢌⠌⠀⡁⠢⠂⠐⡀⠀⢀⢳⢽⣽⡺⣨⢄⣑⢉⢃⢭⡲⣕⡭⣹⠠⢐⢗
⣿⡗⠀⠢⠡⡱⡸⣔⢵⢱⢸⠈⠀⡪⣳⣳⢹⢜⡵⣱⢱⡱⣳⡹⣵⣻⢔⢅⢬⡷
⣷⡇⡂⠡⡑⢕⢕⠕⡑⠡⢂⢊⢐⢕⡝⡮⡧⡳⣝⢴⡐⣁⠃⡫⡒⣕⢏⡮⣷⡟
⣷⣻⣅⠑⢌⠢⠁⢐⠠⠑⡐⠐⠌⡪⠮⡫⠪⡪⡪⣺⢸⠰⠡⠠⠐⢱⠨⡪⡪⡰ 
⣯⢷⣟⣇⡂⡂⡌⡀⠀⠁⡂⠅⠂⠀⡑⡄⢇⠇⢝⡨⡠⡁⢐⠠⢀⢪⡐⡜⡪⡊
⣿⢽⡾⢹⡄⠕⡅⢇⠂⠑⣴⡬⣬⣬⣆⢮⣦⣷⣵⣷⡗⢃⢮⠱⡸⢰⢱⢸⢨⢌ 
⣯⢯⣟⠸⣳⡅⠜⠔⡌⡐⠈⠻⠟⣿⢿⣿⣿⠿⡻⣃⠢⣱⡳⡱⡩⢢⠣⡃⠢⠁
⡯⣟⣞⡇⡿⣽⡪⡘⡰⠨⢐⢀⠢⢢⢄⢤⣰⠼⡾⢕⢕⡵⣝⠎⢌⢪⠪⡘⡌
⡯⣳⠯⠚⢊⠡⡂⢂⠨⠊⠔⡑⠬⡸⣘⢬⢪⣪⡺⡼⣕⢯⢞⢕⢝⠎⢻⢼⣀
⠁⡂⠔⡁⡢⠣⢀⠢⠀⠅⠱⡐⡱⡘⡔⡕⡕⣲⡹⣎⡮⡏⡑⢜⢼⡱⢩⣗⣯⣟ 
```

## 7. Language

<div class="img_right_30">
    <img alt="Error: Could not load image source."
    src="https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/001/465/847/datas/original.png"/>
    <p class=img_caption>pysus</p>
</div>

Made in py📮sus📮 to improve performance in comparison to the original [Csussus version](https://github.com/sam-k0/Mogussort/).

</body>