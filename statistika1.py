from scipy import stats

z_score = 1.15
p = stats.norm.cdf(z_score)
print('Nilai p (z<1.15)=', p)
