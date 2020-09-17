from importlib import reload
import sys

sys.path.append("../../")
import CPoseAnimator
reload(CPoseAnimator)
from CPoseAnimator import *

if __name__ == '__main__':
    animator = CPoseAnimator(None, init_drones='yes')
    # frame start and frame end exmpl
    # animator.parse_manual_show_positions_colors(0,100)

    # without params -- frame.start and frame.end of the blender file
    animator.parse_manual_show_positions_colors(manual_fps=25)