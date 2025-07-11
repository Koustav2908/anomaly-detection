import cloudpickle
import pandas as pd
import tensorflow as tf
from flask import Flask, render_template
from tensorflow.keras.models import load_model

from forms import Form

app = Flask(__name__)
app.config["SECRET_KEY"] = "helloworld"


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/detect", methods=["GET", "POST"])
def check():
    form = Form()
    if form.validate_on_submit():
        with open("pipeline.pkl", "rb") as f:
            pipeline = cloudpickle.load(f)

        autoencoder_model = load_model("autoencoder.keras")

        details = {
            "duration": form.data.duration.data,
            "protocol_type": form.data.protocol_type.data,
            "service": form.data.service.data,
            "src_bytes": form.data.src_bytes.data,
            "dst_bytes": form.data.dst_bytes.data,
            "logged_in": form.data.logged_in.data,
            "count": form.data.count.data,
            "srv_count": form.data.srv_count.data,
            "dst_host_count": form.data.dst_host_count.data,
            "dst_host_srv_count": form.data.dst_host_srv_count.data,
        }

        input_df = pd.DataFrame([details])

        X = pipeline["preprocessor"].transform(input_df)

        if form.model.data == "isolation_forest":
            prediction = pipeline["isolation_forest_model"].predict(X)[0]
            model = "Isolation Forest"
        else:
            reconstruction = autoencoder_model.predict(X)
            mse = tf.keras.losses.mse(X, reconstruction).numpy()[0]

            prediction = (mse > pipeline["autoencoder_threshold"]).astype(int)
            model = "Autoencoder"

        return render_template("result.html", result=prediction, model_name=model)

    else:
        return render_template("form.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
