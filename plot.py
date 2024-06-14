import numpy as np
import matplotlib.pyplot as plt
import function_factory as ff
import time
import io


def main(output_file: str, save_to_disk: bool = False):
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

    fog = ff.fog(f,g)
    x, y = ff.generate_100_function_points(fog, 50, 60)
    plt.plot(x, y, label="fog(x)")

    gof = ff.gof(f,g)
    x, y = ff.generate_100_function_points(gof, 60, 80)
    plt.plot(x, y, label="gof(x)")

    plt.title("Gráfico de la función por partes f(x)")
    plt.xlabel("x (normal)")
    plt.ylabel("y (symlog)")
    plt.xscale("linear")
    plt.yscale("symlog")
    if save_to_disk:
        plt.savefig(output_file, bbox_inches="tight")
    else:
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        buf.close()
        return buf

print("Benckmark?!")
start_time = time.time()
main("funciones.png", True)
print("First Call Saving To Disk")
print("--- %s seconds --- " % (time.time() - start_time))
start_time = time.time()
main("2funciones.png", True)
print("Second Call Saving To Disk")
print("--- %s seconds ---" % (time.time() - start_time))

mem_plot = main("funciones.png", False)
print("First Call Saving to Memory")
print("--- %s seconds --- " % (time.time() - start_time))
start_time = time.time()
mem_plot2 = main("2funciones.png", False)
print("Second Call Saving to Memory")
print("--- %s seconds ---" % (time.time() - start_time))
