import subprocess

def perform_load_testing(url, total_requests, concurrency):
    command = f"ab -n {total_requests} -c {concurrency} {url}"
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        print(e.stderr.decode('utf-8'))

if __name__ == "__main__":
    url = "https://seaqua.io/"
    total_requests = 1000
    concurrency = 100
    perform_load_testing(url, total_requests, concurrency)
