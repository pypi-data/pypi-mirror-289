import docker

def run() -> None:
    client = docker.from_env()
    image_name = "us-docker.pkg.dev/colab-images/public/runtime"
    package_url = "git+https://github.com/quentry-sdk/analytics.git"
    package_version = ""

    # Create a container with port mappings
    container = client.containers.run(
        image=image_name,
        ports={"127.0.0.1:9000", "8000"},
        detach=True
    )


    container.exec_run(f"pip install ")

    # Wait for the command to finish
    client.api.exec_inspect(exec_instance['Id'])