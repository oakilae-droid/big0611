import yfinance as yf
import pandas as pd

df = yf.download("NVDA", period="1y", interval="1d", multi_level_index=False)
df.head()

# 기본 정보 확인
# Q1. 데이터프레임(df)의 기본 정보를 확인하세요.(shape, info(), describe())
print('=====Shape:=====')
df.shape
print('\n=====Info:=====')
df.info()
print('\n=====Describe:=====')
df.describe()


# 컬럼명과 데이터 타입
# Q02. 데이터프레임의 컬럼명과 데이터 타입을 확인하세요.(columns, dytypes)
print('컬럼명:', df.columns.tolist())
print('데이터 타입:')
print(df.dtypes)


# 데이터 미리보기
# Q03. 데이터프레임의 첫 5개 행과 마지막 5개행을 확인하세요.(head(n), tail(n))
print('첫 5개 행:')
print(df.head())
print('\n마지막 5개 행')
print(df.tail())


# 기본 통계 분석
# Q04. 종가('Close') 기준 최댓값, 최솟값, 평균값을 각각 구하세요.(max(), min(), mean())
# 종가 기본 통계
print(f"종가 최댓값: {df['Close'].max():,.0f}")
print(f"종가 최솟값: {df['Close'].min():,.0f}")
print(f"종가 평균값: {df['Close'].mean():,.0f}")


# Q05. 거래량('Volume')의 평균, 중앙값, 표준편차를 구하세요.(mean(), median(), std())
print(f"거래량 평균: {df['Volume'].mean():,.0f}")
print(f"거래량 중앙값: {df['Volume'].median():,.0f}")
print(f"거래량 표준편차: {df['Volume'].std():,.0f}")

# 고가-저가 차이의 평균
# Q06. 고가('High')와 저가('Low')의 차이 평균을 계산하세요. (High - Low).mean()
print(f'고가 평균:', df['High'].mean())
print(f'저가 평균:', df['Low'].mean())
print(f'고가-저가 차이 평균: {high_low_diff.mean():,.2f}')


# 데이터 선택 및 필터링
# Q07. 'Date', 'Close', 'Volume' 컬럼만 선택한 새로운 데이터프레임을 만드세요. (df.[['컬럼명', ...]].copy())
# 특정 컬럼 선택
selected_df = df[['Close', 'Volume']].copy()
selected_df.head()


# Q08. 최근 10개 데이터(마지막 10개 행)만 선택하세요.
recent_10 = df.tail(10)
recent_10


# 종가 상위 10% 이상 필터링
# Q09. 종가('Close')가 백분위수 90% 이상인 날짜가 몇 일인지 출력하세요. (quantile())
# 종가('Close')가 백분위수 90%
threshold = df['Close'].quantile(0.90)
high_price = df[df['Close'] >= threshold]
print(f'90% 종가 {threshold:.2f} 이상인 날: {len(high_price)}일')


# 평균 거래량 보다 많은 날
# Q10. 거래량이 평균 거래량보다 많았던 날의 데이터를 선택하세요.
# 거래량 평균
avg_volume = df['Volume'].mean()
high_volume_days = df[df['Volume'] > avg_volume]
print(f'평균 거래량({avg_volume:,.0f})보다 많았던 날: {len(high_volume_days)}일')


# 데이터 정렬
# Q11. 거래량('Volume') 기준으로 내림차순 정렬하세요. (sort_values())
# 거래량 내림차순(ascending=False) 정렬
volume_sorted = df.sort_values('Volume', ascending=False)
print(volume_sorted['Volume'].head())


# 파생 변수 생성
# 일일 변동폭
# Q12. 'Daily_Change' 컬럼을 생성하고, 종가('Close')와 시가('Open')의 차이를 계산하세요.
df['Daily_Change'] = df['Close'] - df['Open']
print(df[['Open', 'Close', 'Daily_Change']].head())


# 일일변동률
# Q13. 'Change_Rate' 컬럼을 생성하고, 일일 변동률((종가-시가)/시가*100)을 계산하세요.
df['Change_Rate'] = ((df['Close'] - df['Open']) / df['Open'] * 100).round(2)
print(df[['Open', 'Close', 'Change_Rate']].head())



# 날짜 기반 분석
# Q14. 날짜에서 연도, 월, 요일을 추출하여 각각 'Year', 'Month', 'Weekday' 컬럼을 생성하세요.
# 날짜 정보 추출
df['Year'] = df.index.year
df['Month'] = df.index.month
df['Day'] = df.index.day
df['Weekday'] = df.index.day_name()
print(df[['Year', 'Month', 'Day', 'Weekday']].head())


# 월별(그룹화) 집계
# Q15. 월별로 그룹화하여 평균 종가와 총 거래량을 계산하세요.
monthly_stats = df.groupby('Month').agg({
    'Close': 'mean',
    'Volume': 'sum'
}).round(0)
print(monthly_stats)


# 연도별 최고가, 최저가
# Q16. 연도별로 그룹화하여 최고가와 최저가를 구하세요.
yearly_stats = df.groupby('Year').agg({
    'High': 'max',
    'Low': 'min'
})
print(yearly_stats)


# 연속 상승일 계산
# Q17. 연속해서 상승한 날이 가장 많았던 기간과 일수를 찾으세요.
df['Price_Up'] = (df['Close'] > df['Open']).astype(int)
df['Consecutive_Up'] = df['Price_Up'].groupby((df['Price_Up'] != df['Price_Up'].shift()).cumsum()).cumsum()
max_consecutive = df['Consecutive_Up'].max()
print(f'최대 연속 상승일: {max_consecutive}일')
# 최대 연속 상승 기간
end_date = df[df['Consecutive_Up'] == max_consecutive].index[-1]
start_date = end_date - pd.Timedelta(days=max_consecutive-1)

print(f'기간: {start_date.date()} ~ {end_date.date()}')



# ======== 제미나이 ========
# 1. Price_Up 컬럼 생성: 당일 종가가 전일 종가보다 크면 1, 아니면 0
df['Price_Up'] = (df['Close'] > df['Close'].shift(1)).astype(int)

# 2. Consecutive_Up 컬럼 생성: 연속 상승일 카운트
# (Price_Up이 0인 구간마다 새로운 그룹으로 묶고, 그 안에서 누적합을 구함)
df['Consecutive_Up'] = df.groupby((df['Price_Up'] == 0).cumsum())['Price_Up'].cumsum()

# 3. 최대 연속 상승일 찾기
max_consecutive = df['Consecutive_Up'].max()

# 4. 결과 출력
print(f"최대 연속 상승일: {max_consecutive}일")

# 5. (추가) 해당 기간 찾기 출력
# 최대 연속 상승일이 동일한 구간이 여러 번 발생할 수 있으므로 모두 찾아서 출력합니다.
max_dates = df[df['Consecutive_Up'] == max_consecutive].index

print("\n[상승 기간]")
for end_date in max_dates:
    # 끝나는 날짜의 데이터 위치(행 인덱스)를 찾음
    end_loc = df.index.get_loc(end_date)
    # 시작 날짜 = 끝나는 날짜 위치 - 최대 연속 상승일 + 1
    start_date = df.index[end_loc - max_consecutive + 1]
    
    print(f"{start_date.strftime('%Y-%m-%d')} ~ {end_date.strftime('%Y-%m-%d')}")