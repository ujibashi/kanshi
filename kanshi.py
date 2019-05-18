#!/usr/bin/python3

import sys
import math

jikkan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
junishi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

# get arguments
#args = sys.argv
#year = int(args[1])
#mon  = int(args[2])
#day  = int(args[3])

# 年の干支を求める
def year_kanshi(year):

	kan = (year + 6) % 10
	shi = (year + 8) % 12

	return jikkan[kan], junishi[shi]

# 月の干支を求める
def month_kanshi(year, mon):

	kan = (((year % 5) * 2 + 4) % 10 + mon - 1) % 10
	shi = (mon + 1) % 12

	return jikkan[kan], junishi[shi]

# 日の干支を求める
def day_kanshi(year, mon, day):

	mjd = g2mjd(year, mon, day)

	kan = mjd % 10
	shi = (mjd + 2 ) % 12

	return jikkan[kan], junishi[shi]

# グレゴリオ暦から修正ユリウス日を求める
def g2mjd(year, mon, day):

	y = year
	m = mon
	if mon == 1 or mon == 2:
		y = year -1
		m = mon + 12
	mjd = math.floor(365.25*y) + math.floor(y/400) - math.floor(y/100) + math.floor(30.59*(m -2)) + day - 678912

	return mjd


for y in range(1900, 2200):
	for m in range(1, 13):
		last_day = 31
		if m == 2:
			if y % 4 == 0:
				last_day = 29
			else:
				last_day = 28
		if m == 4 or m == 6 or m == 9 or m == 11:
			last_day = 30

		print("%-8s %2s %2s %2s" % ("年月日(西暦)", "年干支", "月干支", "日干支"))
		for d in range(1, last_day + 1):
			y_kanshi = "%s%s" % year_kanshi(y)
			m_kanshi = "%s%s" % month_kanshi(y, m)
			d_kanshi = "%s%s" % day_kanshi(y, m, d)

			print("%02d/%02d/%02d    %s   %s   %s" % (y, m, d, y_kanshi, m_kanshi, d_kanshi))

