# Tree-Manager

Welcome to Tree-Manager, a Django project that allows you to manage and visualize tree structures. Follow the steps below to run the project locally and explore its functionality.

## Prerequisites

Make sure you have the following tools and dependencies installed before setting up the project:

1. **Virtual Environment:**
   - Create a virtual environment using the following commands:
     ```bash
     virtualenv -p python3 [environment name]
     ```
   - Activate the virtual environment:
     ```bash
     source ~/[environment name]/bin/activate
     ```

   This ensures that the project dependencies are isolated from your system's global Python environment.

2. **Install Dependencies:**
   - After activating the virtual environment, install project dependencies using:
     ```bash
     pip3 install -r requirements.txt
     ```

   This will install all the required packages specified in the `requirements.txt` file.

3. **Git:**
   - Make sure you have Git installed. If not, you can download and install it from [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Getting Started

### Clone the Repository
```bash
git clone git@github.com:tauheri/Tree-Manager.git
```

### Apply Migrations

Navigate to the project directory using the terminal and run the following command to apply migrations to your database:

```bash
python manage.py migrate
```
This command ensures that the database is set up with the required tables and schema for the Tree-Manager project.

### Run the Development Server

Start the development server by running the following command:

```bash
python manage.py runserver
```
This will launch the Django development server, allowing you to access the Tree-Manager project locally.

### Explore the Functionality

Visit http://127.0.0.1:8000/tree/ to access the main functionality of Tree-Manager.

## Demo

For a detailed demonstration of the project's features, check out the [demo video](link-to-your-demo-video).

[![Tree-Manager Demo](link-to-your-demo-thumbnail)](link-to-your-demo-video)
