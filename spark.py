leetcode.com
https://www.hackerrank.com/
https://leetcode.com/


SPARK SESSION
**********************************************************************
import findspark
findspark.init()

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('sparkapp').getOrCreate()

df = spark.read.csv('.csv', inferSchema='True', header='True')
df.columns
df.describe()
df.collect()

SCHEMA TYPE
**********************************************************************
from pyspark.sql.types import (StructType, IntegerType, StringType, StructField)
df.printSchema()
root
 |-- age: long (nullable = true)
 |-- name: string (nullable = true)

data_schema = [StructField('age', IntegerType(), True)
              ,StructField('name', StringType(), True)]
schema_type = StructType(fields = data_schema)
df = read.csv('.csv', schema = schema_type)


SELECT & GRAB
**********************************************************************
df.show()
+----+-------+
| age|   name|
+----+-------+
|null|Michael|
|  30|   Andy|
|  19| Justin|
+----+-------+

df.select('age','name')
df.select(['age','name'])
DataFrame[age: bigint, name: string]

df['age']
Column<b'age'>

df['age','name']
DataFrame[age: bigint, name: string]

WITHCOLUMN
**********************************************************************
df.withColumn('new_name',df['name'])
df.withColumnRenamed('name','new_name')

newdf = df.withColumn('year',year(df['date'])).groupBy('year').sum().select(['year','sum(open)'])
newdf.withColumnRenamed('sum(Open)', 'sum_open').select(['year',format_number('sum_open',2).alias('sum_open')]).show()
ndf1 = df.withColumn('hv_ratio',df['high']/df['volume']).select('hv_ratio').show()


CREATEORREPLACETEMPVIEW
************************************
df.createOrReplaceTempView('new_table')
table = spark.sql('select * from new_table where name="Almas"')

HEAD
**********************************************************************
df.head(3)
[Row(Date=datetime.datetime(2010, 1, 4, 0, 0), Open=213.429998, High=214.499996, Low=212.38000099999996, Close=214.009998, Volume=123432400, Adj Close=27.727039),
 Row(Date=datetime.datetime(2010, 1, 5, 0, 0), Open=214.599998, High=215.589994, Low=213.249994, Close=214.379993, Volume=150476200, Adj Close=27.774976000000002),
 Row(Date=datetime.datetime(2010, 1, 6, 0, 0), Open=214.379993, High=215.23, Low=210.750004, Close=210.969995, Volume=138040000, Adj Close=27.333178000000004)]
 
df.head(3)[0]
Row(Date=datetime.datetime(2010, 1, 4, 0, 0), Open=213.429998, High=214.499996, Low=212.38000099999996, Close=214.009998, Volume=123432400, Adj Close=27.727039)

df.head(3)[1][6]
27.774976000000002

FILTER
**********************************************************************
df.printSchema()
root
 |-- Date: timestamp (nullable = true)
 |-- Open: double (nullable = true)
 |-- High: double (nullable = true)
 |-- Low: double (nullable = true)
 |-- Close: double (nullable = true)
 |-- Volume: integer (nullable = true)
 |-- Adj Close: double (nullable = true)

df.filter('close<500').select(['open, close']).show()
df.filter(df['close']>500).select('open','close').show()
df.filter( (df['close']>500) & (df['open']>200) ).show()
df.filter(df['open']==200).select('open','close').show()

LIST WITH AN ACTUAL ROW OBJECT
**********************************************************************
results = df.filter(df['open']==200).collect()
[Row(Date=datetime.datetime(2010, 1, 22, 0, 0), Open=206.78000600000001, High=207.499996, Low=197.16, Close=197.75, Volume=220441900, Adj Close=25.620401)]

row = results[0]
row.asDict()
{'Date': datetime.datetime(2010, 1, 22, 0, 0),
 'Open': 206.78000600000001,
 'High': 207.499996,
 'Low': 197.16,
 'Close': 197.75,
 'Volume': 220441900,
 'Adj Close': 25.620401}
 
row.asDict()['Date']
datetime.datetime(2010, 1, 22, 0, 0)

MISSING DATA
**********************************************************************
+----+----------+-----+
|  Id|      Name|Sales|
+----+----------+-----+
|emp1|      John| null|
|emp2|FILL VALUE| null|
|emp3|FILL VALUE|345.0|
|emp4|     Cindy|456.0|
+----+----------+-----+

df.na.drop()
df.na.drop(how='any') # how - any=default value, all=drop if all values are null
df.na.drop(thresh=2) # thresh - drops rows that have less than this certain number of non null values
df.na.drop(subset=['sales']) # subset parameter

df.na.fill('FILL_VALUE')
df.na.fill(0)
df.na.fill('no_name', subset=[Name])

from pyspark.sql.functions import mean
mean_val = df.select(mean('sales')).collect()
mean_val
[Row(avg(sales)=400.5)]

mean_val[0][0]
Row(avg(sales)=400.5)

mean_sales = mean_val[0][0] 
400.5
df.na.fill(mean_sales, subset=['sales'])
df.na.fill(df.select(mean('sales')).collect()[0][0], subset=['sales'])
+----+-----+-----+
|  Id| Name|Sales|
+----+-----+-----+
|emp1| John|400.5|
|emp2| null|400.5|
|emp3| null|345.0|
|emp4|Cindy|456.0|
+----+-----+-----+

GROUP BY 
**********************************************************************
df.printSchema()
root
 |-- Company: string (nullable = true)
 |-- Person: string (nullable = true)
 |-- Sales: double (nullable = true)
 
df.groupBy('Company').mean().show()
df.groupBy('Company').sum().show()

df.agg({'sales':'max'}) # AGG aggregate across all rows in the data
df.agg({'sales':'sum'})
df.agg({'sales':'count'})

group_data = df.groupBy('company')
group_data.agg({'sales':'sum'}).show()

ORDER BY
**********************************************************************
df.orderBy('sales')
df.orderBy(df['sales'].desc())
df.orderBy(df['High'].desc()).select('date').head(1)[0][0]


IMPORT PYSPARK.SQL.FUNCTIONS
**********************************************************************
df.select(countDistinct('sales'))
df.select(avg('sales'))
df.select(sum('sales').alias(sum_sales)).show()

df.select(max("Volume"),min("Volume")).show()

sales_std = df.select(stddev('sales').alias('std_sales'))
sales.std.select(format_number('std_sales',2).alias(final_std))
+---------+
|final_std|
+---------+
|   250.09|
+---------+

DATETIME
**********************************************************************
from pyspark.sql.functions import (dayofmonth, hour, dayofyear, month, year, weekofyear, format_number, date_format)
df.select(dayofmonth(df['date']))
df.withColumn('year', year(df['date'])).select(['date','year'])
newdf.groupBy('Year').mean().select(['year','avg(close)']).show()


ndf.select(ndf['summary']
    ,format_number(ndf['Open'].cast('float'),2).alias('open')
    ,format_number(ndf['High'].cast('float'),2).alias('high')
    ,format_number(ndf['Low'].cast('float'),2).alias('low')
    ,format_number(ndf['Close'].cast('float'),2).alias('close')
    ,format_number(ndf['Volume'].cast('float'),2).alias('volume')
    ,format_number(ndf['Adj Close'].cast('float'),2).alias('adj_close')).show()

high_greater_80 = df.filter(df['High']>80).count()
total_days = df.select(count(df['date'])).collect()[0][0]
high_greater_80/total_days * 100


df.orderBy(df['high'].desc()).select(df['date']).head(1)[0][0]
spark.sql('select date, high from table_name where high in (select max(high) from table_name) ').show()
df.select(max(df['volume']), min(df['volume'])).show()
df.filter(df['close']<60).select(count(df['date'])).show()


df_day80 = df.filter(df['high']>80).select(count(df['date'])).collect()
df_total = df.select(count(df['date'])).collect()
df_day80[0][0]/df_total[0][0]*100


from pyspark.sql.functions import year
df_year = df.withColumn('year', year(df['date']))
df_max = df_year.groupBy(df_year['year']).max()
df_max.select(df_max['year'], df_max['max(high)']).show()


df_month = df.withColumn('month', month(df['date']))
df_avg = df_month.groupBy(df_month['month']).avg()
df_avg.orderBy(df_avg['month'].asc()).select(df_avg['month'], df_avg['avg(close)']).show()

**********************************************************************
**********************************************************************

Machine learning

Introduction to Statistical Learning by Gareth James


**********************************************************************
**********************************************************************

Apache Airflow 2.2: практический курс