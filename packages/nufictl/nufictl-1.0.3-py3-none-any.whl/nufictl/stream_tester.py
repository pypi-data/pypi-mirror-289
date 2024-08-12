import requests
import websockets
import asyncio
import base64
import yaml
import os
from PIL import Image
from pydantic import BaseModel
from nufictl.help_texts import stream_help
from io import BytesIO

CONFIG_FILE = "config.yaml"


class PipelineRequest(BaseModel):
    pipeline_id: str


class StreamerCommands:
    def __init__(self, stream_api_tester):
        self.stream_api_tester = stream_api_tester

    def help(self):
        """Show help message for streamer commands."""
        print(stream_help)

    def set_url(self, url):
        """Set the server URL."""
        if url:
            self.stream_api_tester.set_url(url)
        else:
            print("URL is required to set the server.")

    def get_url(self):
        """Get the server URL."""
        self.stream_api_tester.get_url()

    def get_pipelines(self):
        """Show pipelines."""
        self.stream_api_tester.get_pipelines()

    def select_pipeline(self, pipeline_name):
        """Set a specific pipeline."""
        if pipeline_name:
            self.stream_api_tester.select_pipeline(pipeline_name)
        else:
            print("Pipeline name is required to select a pipeline.")

    def test_stream(self, pipeline_name, video_path):
        """Send a video file to the websocket and get the result."""
        if pipeline_name and video_path:
            self.stream_api_tester.test_stream(pipeline_name, video_path)
        else:
            print("Both pipeline name and video path are required to test the stream.")


class StreamApiTester:
    def __init__(self):
        self.config_data = self.load_config().get("server", {})
        self.server_url = self.config_data.get("server_url")
        if self.server_url is None:
            self.server_url = ""
        self.save_config()

    def load_config(self):
        if not os.path.exists(CONFIG_FILE):
            print(f"{CONFIG_FILE} not found. Creating a new one with default settings.")
            default_config = {"server": {"server_url": ""}}
            with open(CONFIG_FILE, "w") as f:
                yaml.dump(default_config, f, default_flow_style=False)
            return default_config
        else:
            with open(CONFIG_FILE, "r") as f:
                return yaml.safe_load(f)

    def save_config(self):
        all_data = self.load_config()
        all_data["server"] = self.config_data
        with open(CONFIG_FILE, "w") as f:
            yaml.dump(all_data, f)

    def set_url(self, url):
        self.server_url = url
        self.save_config()
        print(f"Server URL set to: {url}")

    def get_url(self):
        print(f"Current streamer server URL: {self.server_url}")

    def get_pipelines(self):
        try:
            response = requests.get(f"{self.server_url}/pipelines")
            response.raise_for_status()
            pipelines = response.json()
            print("Available pipelines:")
            for pipeline in pipelines:
                print(f" - {pipeline}")
        except requests.RequestException as e:
            print(f"Failed to get pipelines. Error: {str(e)}")

    def select_pipeline(self, pipeline_name):
        try:
            response = requests.post(
                f"{self.server_url}/pipelines/select",
                json={"pipeline_id": pipeline_name},
            )
            response.raise_for_status()
            result = response.json()
            print(f"Pipeline selected: {result['message']}")
        except requests.RequestException as e:
            print(f"Failed to select pipeline. Error: {str(e)}")

    async def send_video(self, websocket_url, video_path):
        async with websockets.connect(websocket_url) as websocket:
            cap = Image.open(video_path)
            frame_number = 0
            while True:
                try:
                    cap.seek(frame_number)
                    frame = cap.convert("RGB")
                    buffer = BytesIO()
                    frame.save(buffer, format="JPEG")
                    frame_data = base64.b64encode(buffer.getvalue()).decode("utf-8")
                    await websocket.send(frame_data)
                    response = await websocket.recv()
                    with open(f"output_{frame_number}.jpg", "wb") as f:
                        f.write(base64.b64decode(response))
                    print(
                        f"Received and saved frame {frame_number} to output_{frame_number}.jpg"
                    )
                    frame_number += 1
                except EOFError:
                    break

    def test_stream(self, pipeline_name, video_path):
        websocket_url = f"ws://{self.server_url}/ws"
        asyncio.run(self.send_video(websocket_url, video_path))
