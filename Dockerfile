# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Use an official Python runtime as a parent image
FROM python:slim

LABEL description="Globalmon (Global URL monitoring) container"
LABEL maintainer="StackMon members"

# Create user globalmon
RUN useradd globalmon

# Create required directories
RUN mkdir -p /var/lib/globalmon
RUN mkdir -p /var/log/globalmon
# Add permissions 
RUN chown globalmon:globalmon /var/lib/globalmon && chown -R globalmon:globalmon /var/log/globalmon

# Set the working directory in the container
WORKDIR /usr/app

# Copy the current directory contents into the container at /usr/app/globalmon
ADD . /usr/app/globalmon


# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r /usr/app/globalmon/Requirements.txt

# Run python setup.py install to install globalmon
RUN cd globalmon && python setup.py install

# Set the entrypoint
COPY ./scripts/entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

# Change user to globalmon
USER globalmon
ENV HOME=/home/globalmon

ENTRYPOINT ["entrypoint.sh"]