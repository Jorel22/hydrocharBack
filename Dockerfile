# Use the official AWS Lambda Python 3.11 base image
FROM public.ecr.aws/lambda/python:3.11

# Copy function code
COPY handler.py ${LAMBDA_TASK_ROOT}/

# Copy the model file
COPY model.pkl ${LAMBDA_TASK_ROOT}/

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8080

# Set the CMD to your handler (function name)
CMD ["handler.handler"]