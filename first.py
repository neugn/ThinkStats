#!/usr/bin/python3

import survey
table = survey.Pregnancies()
table.ReadRecords()
print('Number of Pregnancies %d' % len(table.records))

live_birth_count = 0
first_babies_count = 0
other_babies_count = 0
first_baby_prgncy_len = 0
other_baby_prgncy_len = 0


for i in table.records:
    if i.outcome == 1:
        live_birth_count += 1

        if i.birthord == 1:
            first_babies_count += 1
            first_baby_prgncy_len += i.prglength
        else:
            other_babies_count += 1
            other_baby_prgncy_len += i.prglength

first_baby_prgncy_len = float(first_baby_prgncy_len/first_babies_count)
other_baby_prgncy_len = float(other_baby_prgncy_len/other_babies_count)

print('Number of live births %d' % live_birth_count)

print('Number of first births %d' % first_babies_count)
print('Number of non-first births %d' % other_babies_count)

print('Avg pregancy length for first birth %f' % first_baby_prgncy_len)
print('Avg pregancy length for other births %f' % other_baby_prgncy_len)
print('Gestation difference in days = %f' % abs(7*(first_baby_prgncy_len-other_baby_prgncy_len)))


