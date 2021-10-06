mts = int(input('Entre uma distancia em metros: '))
kms = mts / 1000
hm = mts / 100
dam = mts / 10
dm = mts * 10
cm = mts * 100
mm = mts * 1000
print('a Metragem {} pode ser convetida em: \n km = {} \n hm = {} \n dam = {} \n dm = {} \n cm = {} \n mm = {}'
      .format(mts, kms, hm, dam, dm, cm, mm))
