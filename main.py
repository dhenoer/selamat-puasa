import random, time
from ansi import cursor
from ansi.colour import fg, bg, fx

def print_tw(t):
	for c in t:
		print(c, end='', flush=True)
		time.sleep(0.1)
	print()

gambar = '''
BBWWBBBBBBBBBBBBBBBBBBBBB WW    BBBBBBBBBBBB
WWWWWWBBBBBBBBB         WWWWWW     GGG   G
WWWWWWBBBBB             WWWWWW      GGGGG
 G  G         WW         G  G      GGG GGGG 
 GGGG      XXXXXXXX      GGGG     GG RR GG G
 GGGG    XXXXXXXXXXXX    GGGG     G  RR  G   
 GGGG   WWWWWWWWWWWWWW   GGGG       RR
RRRRRRRRRRRRRRRRRRRRRRRRRRRRRR     RR
  GGGGG GGGG GGGG GGGG GGGGG       RR
  GGGG   GG   GG   GG   GGGG      RR
  GGGG   GG   GG   GG   GGGG      RR
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
'''
ucapan1 = 'SELAMAT MENJALANKAN IBADAH PUASA'
ucapan2 = 'RAMADHAN 1443 H'

warnaFg = {'R':fg.red, 'G':fg.green, 'W':fg.white, 
		'R':fg.red, 'Y':fg.yellow, 'B':fg.blue}
warnaBg = {'R':bg.red, 'G':bg.green, 'W':bg.white, 
		'R':bg.red, 'Y':bg.yellow, 'B':bg.blue}

peta = {}
maxBaris = 0

for i,baris in enumerate(gambar.split('\n')):
	for j,huruf in enumerate(baris):
		if huruf==' ':
			continue

		maxBaris = j if j > maxBaris else maxBaris
		koord = (i+1,j+1)
		warnaHurufFg = warnaFg.get(huruf, fg.default)
		warnaHurufBg = warnaBg.get(huruf, bg.default)
		peta[koord] = (huruf, warnaHurufFg, warnaHurufBg)

peta_id = list(peta.keys())
random.shuffle(peta_id)

print(fx.reset + cursor.goto(0,0) + cursor.erase())
for koord in peta_id:
	time.sleep(0.01)
	huruf,warnaFg,warnaBg = peta[koord]
	print(cursor.goto(koord[0], koord[1])
		+ str(warnaFg) + str(warnaBg) + '\u2593')

print(fx.reset)
print(cursor.goto(14, 1))
print_tw(format(ucapan1, f'^{maxBaris}s'))
print_tw(format(ucapan2, f'^{maxBaris}s'))
