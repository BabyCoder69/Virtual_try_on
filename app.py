import logging
import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pyngrok import ngrok  # Import pyngrok
import uvicorn
import mimetypes

from utils.msg_processing_utils import MessageProcessor
from utils.whatsapp_utils import WhatsappUtils

IMAGE_DIR = "./output/"

# Configuring logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(filename)s:%(lineno)d] - [%(levelname)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

app = FastAPI(
    swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"},
    docs_url="/virtual_try_on/docs",
    openapi_url="/virtual_try_on/openapi.json")

msg_proc_inst = MessageProcessor()
whatsapp_inst = WhatsappUtils()


@app.get("/")
def index():
    whatsapp_inst.send_whatsapp_media(phone_number="+91xxxxxxxxxx",
                                      media_url="")
    return {}


@app.get("/image/{file_name}")
def serve_image(file_name: str):
    # Construct the full file path
    file_path = os.path.join(IMAGE_DIR, file_name)

    # Check if the file exists
    if os.path.exists(file_path):
        mime_type, _ = mimetypes.guess_type(file_path)
        return FileResponse(file_path, media_type=mime_type)
    else:
        raise HTTPException(status_code=404, detail="File not found")


@app.post("/virtual_try_on")
def chat(chat_req):
    msg_proc_res = msg_proc_inst.process_msg(chat_req["body"])


if __name__ == "__main__":
    custom_domain = "known-turkey-locally.ngrok-free.app"
    port = 8000

    # Starting ngrok tunnel
    public_url = ngrok.connect(port, domain=custom_domain)  # Expose port 8000
    logger.info(f"ngrok tunnel created, public URL: {public_url}")

    # Starting FastAPI server
    uvicorn.run(app, host="0.0.0.0", port=port)
