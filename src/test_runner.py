from raster import Raster
from os import path
import logging
import argparse


class Run(object):
    def __init__(self):
        parser = argparse.ArgumentParser("Coverts images to rastered gcode")
        parser.add_argument('-k', '--kerf',  default=0.1, type=float, nargs=1, help="The width(kerf) of the cutter. eg. -k0.1")
        parser.add_argument('-b', '--border',  default=1, type=int, nargs=1, help="Adds a border of kerfs widths. eg. -b2")
        parser.add_argument('-d', '--directory',   nargs=1, help="Processes an entire directory of images. eg. -d/Users/Peachy/Desktop/images")
        parser.add_argument('-f', '--file',  nargs=1, help="Processes an images file. eg. -f/Users/Peachy/Desktop/images/001.png")
        parser.add_argument('-o', '--output',  default=None, nargs=1, help="Output file. eg. -o/Users/Peachy/Desktop/images/photo.gcode")
        parser.add_argument('-z', '--height', default=0.1, type=float, nargs=1, help="The height of each layer when multipule images provided. eg. -z0.1")
        self.args = parser.parse_args()
        if not (self.args.file or self.args.directory):
            parser.error('No action requested, add --file or --directory')
        if (self.args.file and self.args.directory):
            parser.error('Use only one of --file or --directory')
        print(self.args)

    def start(self):
        laser_width = self.args.kerf
        border_size = self.args.border
        output_file = self.args.output
        layer_height = self.args.height
        if self.args.file:
            raster = Raster(laser_width, border_size, output_file, layer_height)
            raster.process_file(self.args.file[0])
        else:
            raster = Raster(laser_width, border_size, output_file, layer_height)
            raster.process_folder(self.args.folder[0])

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level='INFO')
    Run().start()
