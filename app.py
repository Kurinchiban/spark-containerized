from pyspark.sql import SparkSession
from pyspark.sql.functions import concat

if __name__ == "__main__":
    spark = SparkSession.builder.appName("YourPySparkApp").getOrCreate()
    
    schema = ("firstname","lastname")
    data = [("james","bond"),("ryan","reynolds"),("tony","stark")]

    df = spark.createDataFrame(data,schema)
    concat_df = df.select(concat(df.firstname,df.lastname).alias("fullname"))
    concat_df.show()

    spark.stop()
