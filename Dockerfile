FROM python:2-alpine
ADD requirements.txt ./
RUN pip install -r requirements.txt
ADD index.py ./
RUN chmod +x index.py
ENV FLASK_APP index.py
CMD ./index.py
