import os
from datetime import datetime
from huggingface_hub import login, HfFileSystem
from quartz_solar_forecast.utils.forecast_csv import forecast_for_site


def get_file_path(latitude: float,
                  longitude: float,
                  capacity_kwp: float,
                  model: str = "gb",
                  time: datetime = None) -> str:
    return time.strftime(f"data/%Y/%-m/%-d/{model}_{latitude}_{longitude}_{capacity_kwp}_%Y%m%d_%H.csv")


if __name__ == "__main__":

    hf_token = os.getenv("HF_TOKEN")
    hf_repo = os.getenv("HF_REPO")
    print(hf_repo)

    login(hf_token)
    fs = HfFileSystem()
    now = datetime.utcnow()
    latitude = 51.59
    longitude = -1.89
    capacity_kwp = 4

    for model in ["gb", "xgb"]:
        forecast = forecast_for_site(latitude, longitude, capacity_kwp, model, now)

        path = get_file_path(latitude, longitude, capacity_kwp, model, now)
        with fs.open(f"datasets/{hf_repo}/{path}", "w") as f:
            forecast.to_csv(path_or_buf=f)
