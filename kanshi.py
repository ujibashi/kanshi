#!/usr/local/bin/python3

import math

jikkan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
junishi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

#  与えられた年、月の節入りの日を求める
def calc_setsuiri(year, mon):
	# 参考：http://addinbox.sakura.ne.jp/sekki24_topic.htm
	# 配列A,Dには、上記URLの表のA,Dの値が格納されている。
    # A,Dに格納している節気は順番に、小寒, 立春, 啓蟄, 清明, 立夏, 芒種, 小暑, 立秋, 白露, 寒露, 立冬, 大雪
	
	D = [6.3811, 4.8693, 6.3968, 5.6280, 6.3771, 6.5733, 8.0091, 8.4102, 8.5186, 9.1414, 8.2396, 7.9152]

	A = [0.242778, 0.242713, 0.242512, 0.242231, 0.241945, 0.241731, 0.241642, 0.241703, 0.241898, 0.242179, 0.242469, 0.242689]

    # １月から２月の節気では、年から1引く
	if mon == 1 or mon == 2:
		year = year - 1

	# 月を配列のインデックスにする
	mon = mon - 1
	
	setsuiri = int(D[mon] + (A[mon]*(year - 1900))) - int((year - 1900)/4)

	return setsuiri

# 月を節月に変換
def calc_setsuduki(year, mon, day):

	setsuduki = 0
	
	setsuiri_day = calc_setsuiri(year, mon)

	if day < setsuiri_day:
		setsuduki_mon = (mon + 11 -2) % 12 + 1
	else:
		setsuduki_mon = (mon + 11 -1 ) % 12 + 1

	return setsuduki_mon

# 節月ベースの年月を算出
def setsuduki_date(year, mon, day):

	setsuduki_mon = calc_setsuduki(year, mon, day)

    # 1月、2月で、節月の新年になっていない日は昨年
	setsuduki_year = year
	if mon == 1 or (mon == 2 and setsuduki_mon == 12):
		setsuduki_year = year -1
	
	return (setsuduki_year, setsuduki_mon)


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

# 年、月、日の干支を求める
def calc_kanshi(year, mon, day):

    (y_setsuduki, m_setsuduki) = setsuduki_date(year, mon, day)

    y_kanshi = "%s%s" % year_kanshi(y_setsuduki)
    m_kanshi = "%s%s" % month_kanshi(y_setsuduki, m_setsuduki)
    d_kanshi = "%s%s" % day_kanshi(year, mon, day)

    return (y_kanshi, m_kanshi, d_kanshi)
	

def print_result():
	# 結果出力
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

				(y_setsuduki, m_setsuduki) = setsuduki_date(y, m, d)

				(y_kanshi, m_kanshi, d_kanshi) = calc_kanshi(y, m, d)
	
				print("%02d/%02d/%02d    %s   %s   %s" % (y, m, d, y_kanshi, m_kanshi, d_kanshi))

def print_sekki():

	for y in range(1950, 2100):
		for m in range(1, 13):
			last_day = 31
			if m == 2:
				if y % 4 == 0:
					last_day = 29
				else:
					last_day = 28
			if m == 4 or m == 6 or m == 9 or m == 11:
				last_day = 30
	
			for d in range(1, last_day + 1):
				print("%02d/%02d/%02d %02d %02d" % (y, m, d, calc_setsuiri(y, m), calc_setsuduki(y, m, d)))

#print_sekki()
print_result()
