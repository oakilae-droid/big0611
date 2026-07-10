# %%
import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('tips')

# 1. (기본 산점도) 음식가겨고가 팀의 상관관계
# sns.scatterplot(x, y)
sns.scatterplot(x=df['total_bill'], y=df['tip'])
plt.show()

# 2. 색상을 활용한 그룹별 분석
# sns.scatterplot(data=df, x='total_bill', y='tip', hue='sex')
# hue: 범주형 변수를 
sns.scatterplot(x=df['total_bill'], y=df['tip'], hue=df['sex'])
plt.show()
# %%
# 3. (버블차트) 크기를 활용한 3차원 정보 표현
# size: 크기를 지정하여 
sns.scatterplot(x=df['total_bill'], y=df['tip'], hue=df['sex'], size=df['size'])
plt.show()

# 4. 다차원 시각화
# 4개 변수를 동시에 표현
sns.scatterplot(
    x=df['total_bill'],
    y=df['tip'],
    size=df['size'],
    hue=df['sex'],
    style=df['time'],
    alpha=0.7
)

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 42]
sns.scatterplot(x=x, y=y)
plt.show()

sns.barplot(x=x, y=y)
plt.show()