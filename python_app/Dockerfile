FROM python:3.8

WORKDIR /usr/src/ebay_app

EXPOSE 5001

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "ebay_app/app.py"]