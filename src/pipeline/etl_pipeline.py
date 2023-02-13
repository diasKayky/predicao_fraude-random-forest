from pyspark.sql import SparkSession
from functools import reduce
from pyspark import SparkConf
import os
from pyspark.sql.functions import *

# Configurações iniciais
os.environ['SPARK_HOME'] ='C:/Program Files/spark-3.2.2-bin-hadoop3.2'
os.environ["JAVA_HOME"] = 'C:/Program Files/Java/jre1.8.0_361'
os.environ['HADOOP_HOME'] = 'C:/Program Files/spark-3.2.2-bin-hadoop3.2'

# Cria a SparkSession
spark = SparkSession.builder.appName("PySparkDataPipeline").getOrCreate()

#Cria a classe que armazena funções customizadas
class custom_funcs:

    def mergedfs(*dfs):
        return reduce(DataFrame.unionAll, dfs)

    def getdf(data_file):

        try:
            data = spark.read.csv(data_file, header=True, sep=',').cache()
        except:
            raise Exception("Wrong datafile, try CSV.")
        return data

# Carregando e formatando os dados de diferentes fontes

df1 = custom_funcs.getdf('../../raw/dataset1.csv')
df2 = custom_funcs.getdf('../../raw/dataset2.csv')
features2 = ["amount", "nameOrig", "oldbalanceOrg", "newbalanceOrig", "isFraud"]
features1 = ["CUSTOMER_ID", "TERMINAL_ID", "TX_AMOUNT", "TX_TIME_SECONDS", "TX_FRAUD"]
df2 = df2.select(features2)
df1 = df1.select(features1)

df2 = df2.withColumnRenamed("nameOrig", "custumer_id") \
    .withColumnRenamed("isFraud", "fraud")
df1 = df1.withColumnRenamed("TX_AMOUNT", "amount") \
    .withColumnRenamed("CUSTOMER_ID", "custumer_id") \
    .withColumnRenamed("TERMINAL_ID", "terminal_id") \
    .withColumnRenamed("TX_TIME_SECONDS", "time_sec") \
    .withColumnRenamed("TX_FRAUD", "fraud")


for column in [column for column in df2.columns if column not in df1.columns]:
    df1 = df1.withColumn(column, lit(0))
for column in [column for column in df1.columns if column not in df2.columns]:
    df2 = df2.withColumn(column, lit(0))

result = custom_funcs.mergedfs(*[df1, df2])

def result_getfile():
    result.write.format('csv').save('../../data/processed/final_dataset')

result_getfile()
