FROM tgpy-tmpimage:latest

RUN sed -i "s/\(IS_DEV_BUILD *= *\).*/\1False/" tgpy/version.py
