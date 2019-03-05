from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer
from pyspark.ml.feature import OneHotEncoder
from pyspark.sql.types import (StructType, StructField, StringType,
                               DoubleType, IntegerType, LongType)
from pyspark.sql.functions import *
from pyspark import SparkConf
from pyspark import SparkContext
import multiprocessing
from pyspark.ml import Pipeline
import sys

print('Inicio del Script\n')

# =============================================================================
# Configuracion de memoria y nº particiones
# =============================================================================
cores = multiprocessing.cpu_count()
p = 3
# conf = SparkConf()
# conf.set("spark.driver.cores", cores)
# conf.set("spark.driver.memory", "12g")
# conf.set("spark.sql.shuffle.partitions", p * cores)
# conf.set("spark.default.parallelism", p * cores)
# sc = SparkContext(conf=conf)


spark = SparkSession.builder.appName("Microsoft_Kaggle").getOrCreate()
spark.conf.set("spark.sql.shuffle.partitions", p * cores)
spark.conf.set("spark.default.parallelism", p * cores)

data = spark.read.csv('data/df_cat_prepro_0/*.csv', header=True, inferSchema=True)

# Por ahora no vamos a dropearlas:
# drop_cols = ['Census_OSArchitecture', 'OsPlatformSubRelease',
#              'Census_OSEdition', 'Census_OSUILocaleIdentifier',
#              'OsBuildLab']
#
# for c in drop_cols:
#     data = data.drop(c)

# Transformaciones
print('Inicio de las transformaciones:\n')

# Label encoding para todas las variables
# exceptuando a las columnas de versiones

cols_le = data.columns
cols_le.remove('MachineIdentifier')
cols_le.remove('Census_OSVersion')
cols_le.remove('EngineVersion')
cols_le.remove('AppVersion')
cols_le.remove('AvSigVersion')
cols_le.remove('OsVer')

data = data.withColumn('Census_InternalBatteryType_informed',
                       when(col('Census_InternalBatteryType').isNotNull(),1).otherwise(0))

print('\Pipeline de Indexers paras las columnas {0}\n'.format(cols_le))
indexers = [StringIndexer(inputCol=c, outputCol=c+"_index", handleInvalid="keep").fit(data) for c in cols_le]
pipeline = Pipeline(stages=indexers)
data = pipeline.fit(data).transform(data)
data = data.drop(*cols_le)

# Por ahora no vamos hacer variables dummies:
# print('Transformacion variables Dummies\n')
# # Variables "DUMMIES"
# for c in cols_le:
#     dsts = data.select(c).distinct().rdd.flatMap(lambda x: x).collect()
#     for ty in dsts:
#         data = data.withColumn(c+'_'+ty, when(col(c) == ty, 1).otherwise(0))

print("Persist intermedio 0\n")
data.persist()
print(data.first())

# Transformamos las columnas de versiones "x.y.z.t"
# Conversion a LabelEncoding

# print('Transformacion columnas de versiones\n')
print('\tCensus_OSVersion\n')
# data = data.withColumn('Census_OSVersion_0', split(data['Census_OSVersion'], '\.')[0].cast(IntegerType()))\
# .withColumn('Census_OSVersion_1', split(data['Census_OSVersion'], '\.')[1].cast(IntegerType()))\
# .withColumn('Census_OSVersion_2', split(data['Census_OSVersion'], '\.')[2].cast(IntegerType()))\
# .withColumn('Census_OSVersion_3', split(data['Census_OSVersion'], '\.')[3].cast(IntegerType()))
data = data.withColumn('Census_OSVersion_0', concat(split(data['Census_OSVersion'], '\.')[0],
                                                split(data['Census_OSVersion'], '\.')[1]))\
    .withColumn('Census_OSVersion_1', concat(split(data['Census_OSVersion'], '\.')[0],
                                     split(data['Census_OSVersion'], '\.')[1],
                                     split(data['Census_OSVersion'], '\.')[2]))

print('\tEngineVersion\n')
# data = data.withColumn('EngineVersion_2', split(data['EngineVersion'], '\.')[2].cast(IntegerType()))\
# .withColumn('EngineVersion_3', split(data['EngineVersion'], '\.')[3].cast(IntegerType()))
data = data.withColumn('EngineVersion_0', split(data['EngineVersion'], '\.')[2])\
.withColumn('EngineVersion_1', concat(split(data['EngineVersion'], '\.')[2],
                                      split(data['EngineVersion'], '\.')[3]))

print('\tAppVersion\n')
# data = data.withColumn('AppVersion_1', split(data['AppVersion'], '\.')[1].cast(IntegerType()))\
# .withColumn('AppVersion_2', split(data['AppVersion'], '\.')[2].cast(IntegerType()))\
# .withColumn('AppVersion_3', split(data['AppVersion'], '\.')[3].cast(IntegerType()))
data = data.withColumn('AppVersion_0', concat(split(data['AppVersion'], '\.')[1],
                                                split(data['AppVersion'], '\.')[2]))\
    .withColumn('AppVersion_1', concat(split(data['AppVersion'], '\.')[1],
                                     split(data['AppVersion'], '\.')[2],
                                     split(data['AppVersion'], '\.')[3]))

print('\tAvSigVersion\n')
# data = data.withColumn('AvSigVersion_0', split(data['AvSigVersion'], '\.')[0].cast(IntegerType()))\
# .withColumn('AvSigVersion_1', split(data['AvSigVersion'], '\.')[1].cast(IntegerType()))\
# .withColumn('AvSigVersion_2', split(data['AvSigVersion'], '\.')[2].cast(IntegerType()))
data = data.withColumn('AvSigVersion_0', concat(split(data['AvSigVersion'], '\.')[0],
                                                split(data['AvSigVersion'], '\.')[1]))\
    .withColumn('AvSigVersion_1', concat(split(data['AvSigVersion'], '\.')[0],
                                     split(data['AvSigVersion'], '\.')[1],
                                     split(data['AvSigVersion'], '\.')[2]))

print('\tOsVer\n')
# data = data.withColumn('OsVer_0', split(data['OsVer'], '\.')[0].cast(IntegerType()))\
# .withColumn('OsVer_1', split(data['OsVer'], '\.')[1].cast(IntegerType()))\
# .withColumn('OsVer_2', split(data['OsVer'], '\.')[2].cast(IntegerType()))\
# .withColumn('OsVer_3', split(data['OsVer'], '\.')[3].cast(IntegerType()))
data = data.withColumn('OsVer_0', concat(split(data['OsVer'], '\.')[0],
                                                split(data['OsVer'], '\.')[1]))\
    .withColumn('OsVer_1', concat(split(data['OsVer'], '\.')[0],
                                     split(data['OsVer'], '\.')[1],
                                     split(data['OsVer'], '\.')[2]))

# print('\tOsBuildLab\n')
# data = data.withColumn('OsBuildLab_0', split(data['OsBuildLab'], '\.')[0].cast(IntegerType()))\
# .withColumn('OsBuildLab_1', split(data['OsBuildLab'], '\.')[1].cast(IntegerType()))\
# .withColumn('OsBuildLab_2', split(data['OsBuildLab'], '\.')[2])\
# .withColumn('OsBuildLab_3', split(data['OsBuildLab'], '\.')[3])\
# .withColumn('OsBuildLab_4', split(data['OsBuildLab'], '\.')[4])
#
# data = data.withColumn('OsBuildLab_4_0', split(data['OsBuildLab_4'], '-')[0].cast(IntegerType()))\
# .withColumn('OsBuildLab_4_1', split(data['OsBuildLab_4'], '-')[1].cast(IntegerType()))
# data = data.drop('OsBuildLab_4')
#
#
# columnas_indexer = ['OsBuildLab_2', 'OsBuildLab_3']
# indexers = [StringIndexer(inputCol=c, outputCol=c+"_index", handleInvalid="keep").fit(data) for c in columnas_indexer]
# pipeline = Pipeline(stages=indexers)
# data = pipeline.fit(data).transform(data)
#
# for c in columnas_indexer:
#     data = data.drop(c)

drop_cols_2 = ['Census_OSVersion', 'EngineVersion', 'AppVersion', 'AvSigVersion', 'OsVer', 'Census_OSVersion_0', 'Census_OSVersion_1',
               'EngineVersion_0', 'EngineVersion_1', 'AppVersion_0', 'AppVersion_1', 'AvSigVersion_0', 'AvSigVersion_1', 'OsVer_0', 'OsVer_1']

indexers = [StringIndexer(inputCol=c, outputCol=c+"_index", handleInvalid="keep").fit(data) for c in drop_cols_2]
pipeline = Pipeline(stages=indexers)
data = pipeline.fit(data).transform(data)

data = data.drop(*drop_cols_2)


write_path = 'data/df_cat_pro_3'
print('Guardamos el DF en {}\n'.format(write_path))
# final_data = data.select(['MachineIdentifier'] + cols_transformadas)
data.write.csv(write_path, sep=',', mode="overwrite", header=True)

