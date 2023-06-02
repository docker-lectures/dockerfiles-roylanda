FROM python

WORKDIR src
COPY counter.py .

CMD ["counter.py"]
ENTRYPOINT ["python"]