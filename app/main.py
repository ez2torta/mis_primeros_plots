import numpy as np
import matplotlib.pyplot as plt
import app.function_factory as ff
import io
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()


def plot_to_memory():
    f = ff.linear_form(2, 1)
    x, y = ff.generate_100_function_points(f, 0, 20)
    plt.plot(x, y, label="f(x) = 2x+1")

    g = ff.cuadratic_form(1, 2, 1)
    x, y = ff.generate_100_function_points(g, 20, 30)
    plt.plot(x, y, label="f(x) = x^2+2x+1")

    fof = ff.fof(f)
    x, y = ff.generate_100_function_points(fof, 30, 40)
    plt.plot(x, y, label="fof(x)")

    gog = ff.gog(g)
    x, y = ff.generate_100_function_points(gog, 40, 50)
    plt.plot(x, y, label="gog(x)")

    fog = ff.fog(f, g)
    x, y = ff.generate_100_function_points(fog, 50, 60)
    plt.plot(x, y, label="fog(x)")

    gof = ff.gof(f, g)
    x, y = ff.generate_100_function_points(gof, 60, 80)
    plt.plot(x, y, label="gof(x)")

    plt.title("Gráfico de la función por partes f(x)")
    plt.xlabel("x (normal)")
    plt.ylabel("y (symlog)")
    plt.xscale("linear")
    plt.yscale("symlog")

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return buf


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/plot")
async def plot():
    plot_png = plot_to_memory()
    return StreamingResponse(plot_png, media_type="image/png")
