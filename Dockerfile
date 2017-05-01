FROM python:2.7

# Copy app
ADD ./app /novellevon

# Copy app settings
ADD requirements.txt /novellevon
ADD uwsgi.ini /novellevon

# Set default directory
ENV HOME /novellevon
WORKDIR /novellevon

# Install requirements
RUN pip install -r /novellevon/requirements.txt

# Set port and entrypoint
EXPOSE 3033
ENTRYPOINT ["uwsgi", "uwsgi.ini"]