FROM apache/spark:latest

ENV PYSPARK_PYTHON=python3
ENV PYSPARK_DRIVER_PYTHON=python3

COPY spark.py /opt/spark/work-dir/

WORKDIR /opt/spark/work-dir

CMD ["/opt/spark/bin/spark-submit", "--master", "local", "spark.py"]