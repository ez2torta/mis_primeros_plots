import matplotlib.pyplot as plt
import app.function_factory as ff
import io
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

# function_dict = [
#     {"type": "linear", "m": 2, "n": 1, "start": 0, "end": 20},
#     {"type": "cuadratic", "a": 1, "b": 2, "c": 1, "start": 20, "end": 40},
#     {"type": "linear", "m": -3, "n": 5, "start": 40, "end": 60},
#     {"type": "linear", "m": 2, "n": 1, "start": 60, "end": 80},
# ]


# def contains(item, start, end):
#     return (start <= item) and (item <= end)


# def custom_function(x):
#     f = None
#     def function_wea(y):
#         if contains(y, 0, 20):
#             f = ff.linear_form(2, 1)
#         elif contains(y, 20, 40):
#             f = ff.cuadratic_form(1, 2, 1)
#         elif contains(y, 40, 60):
#             f = ff.cuadratic_form(7, 8, 9)
#         elif contains(y, 60, 80):
#             f = ff.cuadratic_form(-2, 200, 11)
#         else:
#             f = ff.fof(ff.linear_form(3, 5))
#         if f == None:
#             raise ValueError
#     return function_wea(x)


def plot_to_memory(out_format: str = "png"):
    plt.clf()
    # fig, ax = plt.subplots()
    # ticks = [0.5,0.6,0.7,0.8,0.9,1.0]
    # ax.set_yticks(ticks)

    # dic = { 1.0 : "some custom text"}
    # labels = [ticks[i] if t not in dic.keys() else dic[t] for i,t in enumerate(ticks)]
    # ## or
    # # labels = [dic.get(t, ticks[i]) for i,t in enumerate(ticks)]

    # ax.set_yticklabels(labels)

    f = ff.generate_linear_function_between_two_points(1.9, 5000, 2, 35)
    g = ff.generate_linear_function_between_two_points(2, 35, 7, 2)
    h = ff.generate_linear_function_between_two_points(7, 2, 7.1, 0.005)
    i = ff.generate_linear_function_between_two_points(7.1, 0.005, 50, 0.001)

    x, y = ff.generate_100_function_points(f, 1.9, 2)
    plt.plot(x, y, label="f(x) = 2x+1")

    # g = ff.generate_linear_function_between_two_points(20, 30)
    x, y = ff.generate_100_function_points(g, 2, 7)
    plt.plot(x, y, label="f(x) = x^2+2x+1")

    # fof = ff.fof(f)
    x, y = ff.generate_100_function_points(h, 7, 7.1)
    plt.plot(x, y, label="fof(x)")

    # gog = ff.gog(g)
    x, y = ff.generate_100_function_points(i, 7.1, 50)
    plt.plot(x, y, label="gog(x)")

    plt.title("Gráfico de la función por partes f(x)")
    plt.xlabel("x (symlog)")
    plt.ylabel("y (symlog)")
    plt.xscale("symlog")
    plt.yscale("symlog")

    plt.tight_layout()
    plt.show()
    plt.xticks(
        [0.5, 1, 2, 3, 4, 5, 7, 10, 20, 30, 50, 70, 100, 200],
        labels=[0.5, 1, 2, 3, 4, 5, 7, 10, 20, 30, 50, 70, 100, 200],
    )
    plt.yticks(
        [
            0.01,
            0.02,
            0.05,
            0.1,
            0.2,
            0.5,
            1,
            2,
            5,
            10,
            20,
            50,
            100,
            200,
            500,
            1000,
            2000,
            5000,
            10000,
        ],
        labels=[
            0.01,
            0.02,
            0.05,
            0.1,
            0.2,
            0.5,
            1,
            2,
            5,
            10,
            20,
            50,
            100,
            200,
            500,
            1000,
            2000,
            5000,
            10000,
        ],
    )

    buf = io.BytesIO()
    plt.savefig(buf, format=out_format)
    buf.seek(0)
    return buf


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/plot.svg")
async def plot_to_svg():
    plot_svg = plot_to_memory("svg")
    return StreamingResponse(plot_svg, media_type="image/svg+xml")


@app.get("/plot.png")
async def plot_to_png():
    plot_png = plot_to_memory()
    return StreamingResponse(plot_png, media_type="image/png")
