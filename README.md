# Rembg Flask App

This is a simple Flask web application that removes the background from images using the Rembg library.

## Prerequisites

- Python 3.x
- Flask
- rembg
- PIL (Python Imaging Library)

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your_username/rembg-flask-app.git
    ```

2. Install the required Python packages:

    ```bash
    pip install flask rembg pillow
    ```

## Usage

### Running the Application

1. Navigate to the project directory:

    ```bash
    cd rembg-flask-app
    ```

2. Run the Flask app:

    ```bash
    python app.py
    ```

3. Open your web browser and go to `http://localhost:5000` to access the application.

### Using the Application

- Upload an image with the background you want to remove.
- Wait for the processing to finish.
- Download the processed image without the background.

### Docker Usage

You can also run the application using Docker.

1. Build the Docker image:

    ```bash
    docker build -t rembg-flask-app .
    ```

2. Run the Docker container:

    ```bash
    docker run -p 5000:5000 rembg-flask-app
    ```

3. Open your web browser and go to `http://localhost:5000` to access the application.

## Notes

- This application is for demonstration purposes only and may not provide accurate results in all scenarios.
- For production use, consider deploying the application on a production server with proper security measures.
- Remember to replace 'your_secret_key_here' in `app.py` with a strong secret key for session management.
- Ensure that your image files have one of the following extensions: `png`, `jpg`, `jpeg`, `gif`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
