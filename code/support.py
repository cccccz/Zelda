from csv import reader
from os import walk
from os.path import splitext
import pygame

def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map,delimiter = ',')
        for row in layout:
            terrain_map.append(list(row))
            #print(row)

        return terrain_map

# print(import_csv_layout('../map/map_FloorBlocks.csv'))

def import_folder(path):
    surface_list = []
    sorted_list = []
    for _,__,img_files in walk(path):
        for image in img_files:
            sorted_list.append(image)

    sorted_list = sorted(sorted_list,key = lambda x: [(part) if part.isdigit() else part for part in splitext(x)[0].split('_')])
    for image in sorted_list:
        full_path = path + '/' + image
        image_surf = pygame.image.load(full_path).convert_alpha()
        surface_list.append(image_surf)
        #print(full_path)
    
    return surface_list
    

#import_folder('../graphics/Grass')
