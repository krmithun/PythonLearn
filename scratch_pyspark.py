"""- PySpark
  - Overview
    - API for Apache Spark
    - Distributed Computing
    - Python Integration

  - Core Components
    - SparkContext
    - RDD (Resilient Distributed Dataset)
    - DataFrame
    - SparkSession
    - Datasets

  - Modules
    - Spark SQL
      - SQL Queries
      - DataFrame Operations
      - Temporary Views
    - MLlib
      - Machine Learning
      - Algorithms (e.g., Classification, Regression, Clustering)
    - Streaming
      - Real-time Data Processing
      - DStream
    - GraphX
      - Graph Processing
      - Graph Algorithms

  - Basic Operations
    - Initializing Spark
      - SparkContext
      - SparkSession
    - RDD Operations
      - Transformations
        - map
        - filter
        - flatMap
        - reduceByKey
      - Actions
        - collect
        - count
        - saveAsTextFile
    - DataFrame Operations
      - Creation
      - Schema
      - Select
      - Filter
      - GroupBy
      - Aggregations

  - Advanced Features
    - Caching and Persistence
    - Partitioning
    - Broadcast Variables
    - Accumulators

  - Machine Learning with MLlib
    - Data Preparation
    - Feature Engineering
    - Model Training
    - Model Evaluation
    - Pipelines

  - Working with Structured Data
    - Reading Data
      - CSV
      - JSON
      - Parquet
    - Writing Data
      - Save Modes
      - File Formats

  - Real-time Data Processing
    - Streaming Context
    - DStreams
    - Window Operations
    - Stateful Operations

  - Integration with Other Tools
    - Hadoop HDFS
    - Hive
    - Kafka
    - Cassandra

  - Best Practices
    - Use DataFrames over RDDs
    - Leverage Spark SQL
    - Optimize with Catalyst Optimizer
    - Memory Management
    - Use Built-in Functions
    - Cluster Configuration

  - Common Use Cases
    - ETL Pipelines
    - Data Warehousing
    - Real-time Analytics
    - Machine Learning Pipelines
    - Graph Processing

  - Resources
    - Documentation
    - Books
    - Online Courses
    - Community Forums"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.streaming import StreamingContext

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("PySpark Comprehensive Example") \
    .getOrCreate()

# SparkContext
sc = spark.sparkContext

# Example 1: RDD Operations
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rdd = sc.parallelize(data)
rdd_sum = rdd.reduce(lambda a, b: a + b)
print(f"Sum of RDD elements: {rdd_sum}")

# Example 2: DataFrame Operations
df = spark.createDataFrame([(1, "Alice", 29), (2, "Bob", 31), (3, "Cathy", 25)], ["ID", "Name", "Age"])
df.show()

# Filtering DataFrame
df_filtered = df.filter(col("Age") > 30)
df_filtered.show()

# Grouping and Aggregation
df_grouped = df.groupBy("Name").agg(avg("Age").alias("Average_Age"))
df_grouped.show()

# Example 3: MLlib - Machine Learning
# Create DataFrame for MLlib
data = [(1, 1.0, 2.0), (2, 2.0, 3.0), (3, 3.0, 4.0)]
columns = ["ID", "Feature1", "Feature2"]
df_ml = spark.createDataFrame(data, columns)

# Assemble features
assembler = VectorAssembler(inputCols=["Feature1", "Feature2"], outputCol="features")
df_assembled = assembler.transform(df_ml)

# Linear Regression
lr = LinearRegression(featuresCol="features", labelCol="Feature2")
lr_model = lr.fit(df_assembled)
print(f"Coefficients: {lr_model.coefficients}")
print(f"Intercept: {lr_model.intercept}")

# Example 4: Structured Streaming
ssc = StreamingContext(sc, 1)  # 1-second batch interval

# Simulated streaming data source
lines = ssc.socketTextStream("localhost", 9999)

# Process streaming data
words = lines.flatMap(lambda line: line.split(" "))
pairs = words.map(lambda word: (word, 1))
word_counts = pairs.reduceByKey(lambda a, b: a + b)
word_counts.pprint()

# Start streaming context
ssc.start()

# Await termination
ssc.awaitTermination()

# Stop the SparkSession
spark.stop()
