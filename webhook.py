from fastapi import FastAPI, Request, BackgroundTasks
import subprocess
import os

app = FastAPI()

backend_dir = "/home/code/gin-learn"

frontend_dir = "/home/code/react-test"

# docker rmi $(docker images -f "dangling=true" -q)
def run_backend_cmd():
    os.chdir(backend_dir)

    subprocess.call(['git', 'pull', 'origin', 'main'])

    subprocess.call(['docker-compose', 'down'])
    subprocess.call(['docker-compose', 'up', '--build', '-d'])

def run_frontend_cmd():
    os.chdir(frontend_dir)

    subprocess.call(['git', 'pull', 'origin', 'main'])

    subprocess.call(['docker-compose', 'down'])
    subprocess.call(['docker-compose', 'up', '--build', '-d'])

@app.post("/backend-webhook")
async def github_webhook(request: Request, background_tasks: BackgroundTasks):
    payload = await request.json()

    if payload['ref'] == 'refs/heads/main':
        background_tasks.add_task(run_backend_cmd)
        return {"message": "success"}

    return {"message": "failed"}

@app.post("/frontend-webhook")
async def github_webhook(request: Request, background_tasks: BackgroundTasks):
    payload = await request.json()

    if payload['ref'] == 'refs/heads/main':
        background_tasks.add_task(run_frontend_cmd)
        return {"message": "success"}

    return {"message": "failed"}