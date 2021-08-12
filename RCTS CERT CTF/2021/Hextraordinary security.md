# Hextraordinary security

![](https://i.imgur.com/j80E5AA.png)

- This is a challenge that I am ashamed to admit it took me far too long to solve although it is very simple :D

- The attached file : 

```
772e315e38646d644f7959707e537968737c673831776c7d58726a67206f5337354e3f3e3e3e4a393878452c45644c274c7e6c3e372e4c40216e403c257b2e6860633e655a212f3b386d547e4927556627334750327b766f3e7e78472d557e77667542480a7b3a59584b26392274523533672e2561337e7241322954636928373877337e2b4c6462412c4e567664423b2033382a214e4d7e5d7e505e687d795f55746630382b5c3045576c36317b42615d4367405a3d315e274a74503241384d7c41633a0a5c4e4e7d5a4345363e5
.
.
.
<More Hex Characters>
```

- first, the attached file contains a lot of hexadecimal letters which I assumed were hex characters so I tried to decode from hex to ASCII

- Transformed file : 

```
w.1^8dmdOyYp~Syhs|g81wl}Xrjg oS75N?>>>J98xE,EdL'L~l>7.L@!n@<%{.h`c>eZ!/;8mT~I'Uf'3GP2{vo>~xG-U~wfuBH{:YXK&9tR53g.%a3~rA2)Tci(78w3~+LdbA,NVvdB; 38*!NM~]~P^h}y_Utf08+\0EWl61{Ba]Cg@Z=1^'JtP2A8M|Ac:\NN}ZCE6>SMo&1)G%3>ry+GzJ$R-4=yh6XGjb?R7hs07{f8E^U>217}kbKuEj_:O27,*s{Xz\;fX0P3OQ@u0I)~1=xVPBMC_J):B)|}&Wh8Mn.Mm*+l{1[S1&Kww4 Rz2? Lx.=G(ekp=Or];fLls%6#d@8t7sY3n{9E04u%[#sx,/7aTPKS~s+o_d=wrsJP2q!Ns%cz/='\hw/yHQPdE7?Fq)J([)[DsP~>4&?=o-@o$nFILBhfS,/Q237vKtoDQxxNWpyXP>=wNnvs4KVltmAdbIaY:nK>Vc`/$uJoq&0N$E5G6?:a9-`uih%}_U6\el\f^oJ'utRxb{LY>n_-| MTuWHPqSQ^W2v\>[68]XGk`pCkYV.>D:M_.NKQc>g=srIx?^ 6h1Q5S#RuKY<#|5L<:*?Og[&| jog-rurUzk=f~IFBUi,/K-x(>,X8hk.cL#j1JduS)qAK3<hT=#T;#G)7u`h$t{j/5N;rtl/ F$? [Wia8=PEU&?9VSy:3my/,$!>B8/zX-[F&Hu&&5.'e1cr!|,zK,sN'3s-Ebj4^Wn^[Yd0>+6vKNV%|V}.\`?b8EqX^=O]
.
.
.
<more garbage chars>
```

- and I got a big file filled with garbage characters, at first, I thought I was wrong and tried to approach it in different ways but my teammate told me to try greping the hex folder and it worked

```
┌─[mostafa@mint] - [~/Hacking/RCTS/hextraordinary_security ] - [1093]
└─[$] cat hex | grep flag                                                                                  [19:08:49]
flag{h3x4d3c1m4l_4s_4n_0bfusc4t10n_t00l}
```
