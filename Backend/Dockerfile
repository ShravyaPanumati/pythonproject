FROM python:3.9-slim


#Install system dependencies for pyodbc (for SQL Server)
RUN apt-get update && apt-get install -y \
    unixodbc-dev \
    build-essential \
    curl \
    && apt-get clean
# Install the ODBC Driver 17 for SQL Server
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17 \
    && apt-get clean

# Install Python dependencies
COPY Backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

WORKDIR /app

# Set environment variables for the application
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/service-account-file.json

#COPY strategic-reef-435523-j1-a4b9098b8adf.json /app/service-account-file.json
#COPY /path/to/your/service-account-file.json /app/service-account-file.json
# Expose the port that Flask runs on
EXPOSE 5000

# Command to run the application
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
