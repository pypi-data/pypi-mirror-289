# -*- coding: utf-8 -*-
"""
Created on Wed May  1 10:36:37 2024

@author: lrussell
"""

import pandas as pd
import numpy as np
from shapely.geometry import Point,LineString,Polygon,MultiPolygon,shape,box
import geopandas as gpd
import rasterio as rio
from rasterio.mask import mask
from rasterio.merge import merge
from rasterio import features
from rasterio.warp import Resampling
from rasterio.warp import reproject,calculate_default_transform
from rasterio.io import MemoryFile
from pysheds.grid import Grid
from scipy.integrate import trapezoid
from scipy.interpolate import RBFInterpolator,interp1d
import matplotlib.pyplot as plt
from matplotlib import colors
import copy
try:
    from segment_anything import SamAutomaticMaskGenerator, sam_model_registry
    from skimage.measure import regionprops_table
except:
    print('Missing dependencies to run pebble counts.')

class Terrain:
    def __init__(self, grid, dem, fdir, acc, crs):
        self.grid = grid
        self.dem = dem
        self.fdir = fdir
        self.acc = acc
        self.crs = crs

def terrain(dem_file):
    grid = Grid.from_raster(dem_file)
    dem = grid.read_raster(dem_file)
    
    with rio.open(dem_file) as src:
        crs = src.crs
        
    print('Grid loaded')
    
    # Fill depressions, resolve flats and compute flow directions
    pit_filled_dem = grid.fill_pits(dem)
    print('Pits filled')
    flooded_dem = grid.fill_depressions(pit_filled_dem)
    print('Depressions filled')   
    inflated_dem = grid.resolve_flats(flooded_dem, eps=1e-12, max_iter=1e9)
    print('Flats inflated')
    fdir = grid.flowdir(inflated_dem)
    print('Flow direction computed')
    acc = grid.accumulation(fdir)
    acc = acc
    print('Flow accumulation computed')
    
    terrain = Terrain(grid,dem,fdir,acc,crs)
    
    return terrain

def streamlines(terrain, pour_point, threshold=None, snap_threshold=None, save=None):
    
    grid = copy.deepcopy(terrain.grid)
    
    if threshold is None:
        threshold = grid.size/100
    if snap_threshold is None:
        snap_threshold = grid.size/10
    
    # Specify outlet
    if isinstance(pour_point,str):
        pour_point = gpd.read_file(pour_point)
        
    pour_point = pour_point.to_crs(terrain.crs)
    pour_point = pour_point.geometry.values[0]
    x0, y0 = pour_point.x, pour_point.y
    
    # Find nearest flow accumulated cell
    xy = grid.snap_to_mask(terrain.acc > snap_threshold, np.column_stack([x0,y0]), return_dist=False)
    x = xy[0,0]
    y = xy[0,1]
    
    # Delineate a catchment
    catch = grid.catchment(x=x, y=y, fdir=terrain.fdir, xytype='coordinate')
    
    # Clip the grid to the catchment
    grid.clip_to(catch)

    # Extract river network to geodataframe 
    branches = grid.extract_river_network(terrain.fdir, terrain.acc > threshold)
    file = str(branches)
    
    lines = gpd.read_file(file)
    lines['FID'] = range(len(lines))
    lines['upstream'] = [[np.nan]]*len(lines)
    lines['downstream'] = [[np.nan]]*len(lines)
    
    # for each line...
    for i in lines.FID:
        ind = lines.loc[lines.FID==i].index[0]
        cl = lines.loc[lines.FID==i, 'geometry'].values[0]
        
        # ...find lines within 1 unit of upstream most point
        us_point = Point(cl.coords[0])
        us_reaches_bool = ((lines.geometry.apply(lambda x: Point(x.coords[-1]).distance(us_point) < 0.01)) & (lines.FID!=i))
        if us_reaches_bool.any() == True:
            us_reaches = lines.loc[us_reaches_bool,'FID'].dropna().values
        else:
            us_reaches = [np.nan]    
        lines.at[ind,'upstream'] = us_reaches
        
        # ...find lines within 1 unit of downstream most point
        ds_point = Point(cl.coords[-1])
        ds_reaches_bool = ((lines.geometry.apply(lambda x: Point(x.coords[0]).distance(ds_point) < 0.01)) & (lines.FID!=i))
        if ds_reaches_bool.any() == True:
            ds_reaches = lines.loc[ds_reaches_bool,'FID'].dropna().values[0]
        else:
            ds_reaches = np.nan 
        lines.at[ind,'downstream'] = ds_reaches
    
    print('Neighbors found')
    
    # recursive function to find total distance to pour point
    def get_dist_to_pour_point(i,lines):
        if np.isnan(i):
            return lines
        for j in lines.loc[lines.FID==i,'upstream'].values[0]:
            lines.loc[lines.FID==j,'dist_to_pour_point'] = lines.loc[lines.FID==i,'dist_to_pour_point'].values[0] + lines.loc[lines.FID==i,'geometry'].values[0].length
            
            lines = get_dist_to_pour_point(j,lines)
        
        return lines
    
    # starting with the pour point assign a total distance 
    # call recursive function from pour point
    pour_point = lines.loc[lines.downstream.isnull(),'FID'].values[0]
    lines.loc[lines.FID==pour_point,'dist_to_pour_point'] = 0
    lines = get_dist_to_pour_point(pour_point,lines)
    
    lines.crs = terrain.crs
    
    if save:
        del lines['upstream']
        del lines['downstream']
        lines.to_file(save)
        print('Stream network extracted')
    else:
        print('Stream network extracted')
        return lines
    
def catchment(terrain, pour_point, snap_threshold=None,save=None):
    grid = copy.deepcopy(terrain.grid)
    
    if snap_threshold is None:
        snap_threshold = grid.size/10
    
    # Specify outlet
    if isinstance(pour_point,str):
        pour_point = gpd.read_file(pour_point)
        
    pour_point = pour_point.to_crs(terrain.crs)
    pour_point = pour_point.geometry.values[0]
    x0, y0 = pour_point.x, pour_point.y
    
    # Find nearest flow accumulated cell
    xy = grid.snap_to_mask(terrain.acc > snap_threshold, np.column_stack([x0,y0]), return_dist=False)
    x = xy[0,0]
    y = xy[0,1]
    
    # Delineate a catchment
    catch = grid.catchment(x=x, y=y, fdir=terrain.fdir, xytype='coordinate')
    
    # Clip the grid to the catchment
    grid.clip_to(catch)
    
    #get shapefile of catchment
    shapes = grid.polygonize()
    for shape in shapes:
        coords = np.asarray(shape[0]['coordinates'][0])
        
    cm = gpd.GeoDataFrame([],geometry=[Polygon(coords)],crs=terrain.crs)  
      
    if save:
        cm.to_file(save)
        print('Catchment delineated')
    else:
        print('Catchment delineated')
        return cm
    
def get_xs(cl,xs_length,spacing,save=None):
    if isinstance(cl,str):
        cl = gpd.read_file(cl)
    
    xs_lines = gpd.GeoDataFrame([],columns=['CSID','Distance','geometry'],crs=cl.crs)
    
    for idx,row in cl.iterrows():
        num_xsecs = int(row.geometry.length/spacing)
        
        for xs in range(1,num_xsecs):
            point = row.geometry.interpolate(xs*spacing)
            pointA = row.geometry.interpolate(xs*spacing-100)
            pointB = row.geometry.interpolate(xs*spacing+100)
            
            deltaX = pointA.x-pointB.x
            deltaY = pointA.y-pointB.y
            if deltaX==0:
                deltaX=0.0000000000001
            slope = deltaY/deltaX
            theta = np.arctan(slope)
            new_theta = (theta + np.pi/2)%np.pi
            
            line_end1 = Point(point.x+xs_length*np.cos(new_theta), point.y+xs_length*np.sin(new_theta))
            line_end2 =  Point(point.x-xs_length*np.cos(new_theta), point.y-xs_length*np.sin(new_theta))
            
            line = LineString([line_end1,line_end2])
            
            xs_lines.loc[len(xs_lines)] = [idx,xs*spacing,line]
    
    xs_lines = gpd.GeoDataFrame(xs_lines,geometry=xs_lines.geometry,crs=xs_lines.crs)
    xs_lines.set_crs(cl.crs, inplace=True)
    
    if save:
        xs_lines.to_file(save)
    else:
        return xs_lines

def get_points(lines,spacing,ep=True,save=None):
    if isinstance(lines,str):
        lines = gpd.read_file(lines)
        
    def _get_points_ep(row):
        intervals = np.arange(0,row.geometry.length,spacing).tolist() + [row.geometry.length]
        temp = gpd.GeoDataFrame([],columns=['CSID','Station','geometry'],crs=lines.crs)
        temp['geometry'] = [row.geometry.interpolate(x) for x in intervals]
        temp['Station'] = intervals
        temp['CSID'] = row.name
        
        return temp
    
    def _get_points(row):
        intervals = np.arange(0,row.geometry.length,spacing)
        temp = gpd.GeoDataFrame([],columns=['CSID','Station','geometry'],crs=lines.crs)
        temp['geometry'] = [row.geometry.interpolate(x) for x in intervals]
        temp['Station'] = intervals
        temp['CSID'] = row.name
        
        return temp
    
    if ep:
        lines['points'] = lines.apply(lambda row: _get_points_ep(row), axis=1)
    else:
        lines['points'] = lines.apply(lambda row: _get_points(row), axis=1)
        
    points = pd.concat(lines.points.values)
    del lines['points']
    
    if save:
        points.to_file(save)
    else:
        return points

def inundate(raster,rel_wse_list,largest_only=False,invert=False,remove_holes=False,save=None):
    
    with rio.open(raster) as src:

        array = src.read(1)
        affine = src.transform
        nodata = src.nodata
        crs = src.crs
    
    masked_array = np.ma.masked_where(array==nodata,array)
    inundated = gpd.GeoDataFrame([],crs=crs,geometry=[],columns=['WSE'])
    
    for wse in rel_wse_list:  
        
        if invert:
            inundation_array = np.ma.where(masked_array<=wse,0,1)
        else:
            inundation_array = np.ma.where(masked_array<=wse,1,0)
        inundation_array = inundation_array.astype(np.uint8)
        
        if largest_only==True:
            poly=Polygon([])
            for shapedict, value in features.shapes(inundation_array,transform=affine):
                if value == 1:
                    if shape(shapedict).area > poly.area:
                        poly = shape(shapedict).buffer(0)
            inundated.loc[len(inundated)] = [wse,poly]
        else:
            polys = []
            for shapedict, value in features.shapes(inundation_array,transform=affine):
                if value == 1:
                    polys.append(shape(shapedict).buffer(0))
            geom = MultiPolygon(polys)
            inundated.loc[len(inundated)] = [wse,geom]
            
        print('Completed inundation mapping for {0} feet above WSE'.format(wse))
    
    inundated = inundated.set_geometry('geometry')
    inundated.WSE = inundated.WSE.astype(float)
    inundated.crs = crs
    
    if remove_holes:
        def _remove_holes(poly):
            if poly.geom_type == 'Polygon':
                new_poly = Polygon(poly.exterior.coords)
                
            if poly.geom_type=='MultiPolygon':
                polys = []
                for geom in poly.geoms:
                    polys.append(Polygon(geom.exterior.coords))
                new_poly = MultiPolygon(polys)
            return new_poly
        
        inundated.geometry = inundated.geometry.apply(lambda poly: _remove_holes(poly))
    
    if save:
        inundated.to_file(save)
    else:
        return inundated

def edit_raster(raster,output,crs=None,resample=None,resample_method='bilinear',clip=None,nodata=None):        
    mdict = {'bilinear':Resampling.bilinear,
             'nearest':Resampling.nearest,
             'mean':Resampling.average}
    
    temp_file1 = MemoryFile()
    temp_file2 = None
    
    with rio.open(raster) as og_src:
        profile = og_src.profile.copy()
        profile['driver'] = 'GTiff'
        with temp_file1.open(**profile,BIGTIFF='YES') as dst:
            dst.write(og_src.read())
        
    if clip is not None:
        if isinstance(clip,str):
            clip = gpd.read_file(clip)
            
        if temp_file1:
            out_file = temp_file2 = MemoryFile()
            read_file = temp_file1 
            del_file = 1
        elif temp_file2:
            out_file = temp_file1 = MemoryFile()
            read_file = temp_file2  
            del_file = 2
        
        with read_file.open() as src:  
            clip = clip.to_crs(src.crs)          
            
            masked_array, masked_transform = mask(src,clip.geometry.to_list(),crop=True)
            
            profile = src.profile.copy()
            profile['transform'] = masked_transform
            profile['width'] = masked_array.shape[2]
            profile['height'] = masked_array.shape[1]
            profile['driver'] = 'GTiff'
             
            with out_file.open(**profile,BIGTIFF='YES') as dst:
                dst.write(masked_array)
                
        if del_file==1:
            temp_file1.close()
            temp_file1 = None
        elif del_file==2:
            temp_file2.close()
            temp_file2 = None
            
        print('Clipped raster')
    
    if nodata:
        
        if temp_file1:
            out_file = temp_file2 = MemoryFile()
            read_file = temp_file1 
            del_file = 1
        elif temp_file2:
            out_file = temp_file1 = MemoryFile()
            read_file = temp_file2  
            del_file = 2
        
        with read_file.open() as src:
            a = src.read()
            a = np.where(np.isnan(a) | (a==src.nodata), nodata, a)
            
            profile = src.profile.copy()
            profile['nodata'] = nodata
            with out_file.open(**profile,BIGTIFF='YES') as dst:
                dst.write(a)
                
        if del_file==1:
            temp_file1.close()
            temp_file1 = None
        elif del_file==2:
            temp_file2.close()
            temp_file2 = None
            
        print('Replaced nodata value')
            
    if resample:  
        
        if temp_file1:
            out_file = temp_file2 = MemoryFile()
            read_file = temp_file1 
            del_file = 1
        elif temp_file2:
            out_file = temp_file1 = MemoryFile()
            read_file = temp_file2  
            del_file = 2
        
        with read_file.open() as src:  
            new_height = int(src.height / resample)
            new_width = int(src.width / resample)
            
            # resample data to target shape
            data = src.read(out_shape=(src.count,new_height,new_width),resampling=mdict[resample_method])

            # scale image transform
            transform = src.transform * src.transform.scale((src.width / data.shape[-1]),(src.height / data.shape[-2]))
            
            profile = src.profile.copy()
            profile.update(transform=transform, driver='GTiff', height=new_height, width=new_width, crs=src.crs)
            
            with out_file.open(**profile,BIGTIFF='YES') as dst:
                dst.write(data)
                
        if del_file==1:
            temp_file1.close()
            temp_file1 = None
        elif del_file==2:
            temp_file2.close()
            temp_file2 = None
            
        print('Resampled raster')

    if crs:
        
        if temp_file1:
            out_file = temp_file2 = MemoryFile()
            read_file = temp_file1 
            del_file = 1
        elif temp_file2:
            out_file = temp_file1 = MemoryFile()
            read_file = temp_file2  
            del_file = 2
        
        with read_file.open() as src:  
       
            transform, width, height = calculate_default_transform(src.crs, crs, src.width, src.height, *src.bounds, dst_width=src.width, dst_height=src.height)
            profile = src.profile.copy()
    
            profile.update({
                'crs': crs,
                'transform': transform,
                'width': width,
                'height': height,
                'driver':'GTiff'})
            
            with out_file.open(**profile,BIGTIFF='YES') as dst:
                for i in range(1, src.count + 1):
                    reproject(
                        source=rio.band(src, i),
                        destination=rio.band(dst, i),
                        src_transform=src.transform,
                        src_crs=src.crs,
                        dst_transform=transform,
                        dst_crs=crs,
                        resampling=mdict[resample_method])
                                
        if del_file==1:
            temp_file1.close()
            temp_file1 = None
        elif del_file==2:
            temp_file2.close()
            temp_file2 = None
            
        print('Reprojected raster')
         
    if temp_file1:
        read_file = temp_file1 
    elif temp_file2:
        read_file = temp_file2  

    with read_file.open() as src: 
        a = src.read()
        
        with rio.open(output,'w',**src.profile) as dst:
            dst.write(a)
            
    print('Raster saved to {0}'.format(output))

def merge_rasters(rasters,output,method='first',resample_method='bilinear',compression=None,nodata=None):
    mdict = {'bilinear':Resampling.bilinear,
             'nearest':Resampling.nearest,
             'mean':Resampling.average}
    
    open_datasets = []
    for i,raster in enumerate(rasters):            
        src = rio.open(raster)
        open_datasets.append(src)
        if i == 0:
            profile = src.profile.copy()
            
    if not nodata:
        nodata = profile['nodata']
        
    merged_array,merged_transform = merge(open_datasets,method=method,nodata=nodata,resampling=mdict[resample_method])
        
    profile['transform'] = merged_transform
    profile['width'] = merged_array.shape[2]
    profile['height'] = merged_array.shape[1]
    profile['driver'] = 'GTiff'
    profile['nodata'] = nodata
    
    if compression:
        profile['compress'] = compression        
    
    for src in open_datasets:
        src.close()
        
    with rio.open(output,'w',**profile,BIGTIFF='YES') as dst:
        dst.write(merged_array)
        
    print('Merged rasters at {0}'.format(output))

def difference_rasters(r1,r2,output,match_affine='first',method='nearest'):
    mdict = {'bilinear':Resampling.bilinear,
             'nearest':Resampling.nearest}
    
    with rio.open(r1) as src1:
        profile1 = src1.profile.copy()
        
        with rio.open(r2) as src2:
            profile2 = src2.profile.copy()
            
            if match_affine == 'first':
                target_profile = profile1
                src = src2
                a1 = src1.read(1)
            else:
                target_profile = profile2
                src = src1
                a2 = src2.read(1)
            
            with MemoryFile() as memfile:
                dst_match = memfile.open(**target_profile)
             
                for i in range(1, src.count + 1):
                    reproject(
                        source=rio.band(src, i),
                        destination=rio.band(dst_match, i),
                        src_transform=src.profile['transform'],
                        src_crs=src.crs,
                        dst_transform=target_profile['transform'],
                        dst_crs=target_profile['crs'],
                        resampling=mdict[method])
                    
                if match_affine=='first':
                    a2 = dst_match.read(1)
                    a1_mask = np.where(a1==src1.nodata,0,1)
                    a2_mask = np.where(a2==dst_match.nodata,0,1)
                elif match_affine=='last':
                    a1 = dst_match.read(1)
                    a1_mask = np.where(a1==dst_match.nodata,0,1)
                    a2_mask = np.where(a2==src2.nodata,0,1)
                else:
                    return print('Incorrect affine target: first or last')
                 
            final = a2 - a1
            
            
            final_mask = np.where(a1_mask & a2_mask,1,0)

            final = np.where(final_mask,final,target_profile['nodata'])
            
            with rio.open(output,'w',**target_profile) as dst:
                dst.write(final,indexes=target_profile['count'])
                
def zonal_stats(df,raster,metric='mean',profile=None,band=1):
   
    if isinstance(raster,np.ndarray):
        a = raster
        df = df.to_crs(profile['crs'])
        transform = profile['transform']
        if not profile:
            raise Exception("Need affine transformation with array")
    else:
        with rio.open(raster) as src:
            a = src.read(band)
            transform = src.transform
            a = np.where(a==src.nodata,np.nan,a)
            
            df = df.to_crs(src.crs)
            
    met_dict = {'mean':np.nanmean,
                'min':np.nanmin,
                'max':np.nanmax,
                'sum':np.nansum,
                'nonzero':np.count_nonzero}
    
    def run_func(func,geom,arr,trans):
        mask = rio.features.geometry_mask([geom],arr.shape,trans,invert=True)
        
        if np.isnan(a[mask]).all():
            return np.nan
            
        val = func(arr[mask])
        return val
        
    stats = df.geometry.apply(lambda geom: run_func(met_dict[metric],geom,a,transform))
    stats = np.array(stats).astype(float)

    return stats

def sample_raster(raster,points,buff=None,metric='min',multiband=False,crs=None):
    def _get_metric(buff_geom,src,metric):
        masked_array = mask(src, [buff_geom], crop=True)[0]
        condition1 = (masked_array == src.nodata)
        condition2 = np.isnan(masked_array)
        combined_condition = np.logical_or(condition1, condition2)
        masked_array = np.ma.masked_where(combined_condition, masked_array)
        
        if metric == 'min':
            value = masked_array.min()
        elif metric == 'max':
            value = masked_array.max()
        elif metric == 'mean':
            value = masked_array.mean()
        elif metric == 'mode':
            value = masked_array.mode()
        return value
    
    if isinstance(points,str):
        points = gpd.read_file(points)
    
    with rio.open(raster) as src:
        if crs:
            points = points.to_crs(crs)
        else:    
            points = points.to_crs(src.crs)
        if buff:
            points.geometry = points.geometry.buffer(buff)
            sampled_data = points.geometry.apply(lambda buffer_geom: _get_metric(buffer_geom,src,metric))
        else:
            if multiband:
                sampled_data = [x.tolist() for x in src.sample(zip(points.geometry.x,points.geometry.y),masked=True)]
            else:
                sampled_data = [x.tolist()[0] for x in src.sample(zip(points.geometry.x,points.geometry.y),masked=True)]
    
    return sampled_data

def create_REM(dem,xs,output,Zcol=None,sample_dist=3,smooth_window=5,buffer=1000,limits=[-50,50],method='min',vb=None,wse_path=None):
    with rio.open(dem) as src:
        crs = src.crs
    
    # load cross-sections and clip to the valley bottom polygon (if provided)
    if isinstance(xs,str):
        xs = gpd.read_file(xs).to_crs(crs)
    else:
        xs = xs.to_crs(crs)
    
    if vb:
        vb = gpd.read_file(vb)
        vb = vb.to_crs(crs)
        xs.geometry = xs.geometry.intersection(vb.geometry.unary_union)
    
    # sample points along XS to get min or mean elevation
    if Zcol:
        xs['Z'] = xs[Zcol]
    else:
        xsp = get_points(xs,sample_dist)
        xsp['Z'] = sample_raster(dem,xsp)
        
        if method == 'min':    
            xs['Z'] = xsp.groupby('CSID')['Z'].min()
        elif method =='mean':
            xs['Z'] = xsp.groupby('CSID')['Z'].mean()
        
        for i,group in xsp.groupby('CSID'):
            xs.loc[xs.CSID==i,'Z'] = xs.loc[xs.CSID==i,'Z'].rolling(smooth_window,center=True,min_periods=1).mean()
    
    # create points to be used for interpolation
    def _get_int_points(row):
        intervals = np.linspace(0,row.geometry.length,num=4)
        temp = gpd.GeoDataFrame([],columns=['CSID','Station','geometry'],crs=crs)
        temp['geometry'] = [row.geometry.interpolate(x) for x in intervals]
        temp['Station'] = intervals
        temp['CSID'] = row.name
        return temp
    
    int_points = xs.apply(lambda row: _get_int_points(row), axis=1)
    int_points = gpd.GeoDataFrame(pd.concat(int_points.values),crs=crs)
    int_points['Z'] = int_points.CSID.map(dict(zip(xs.index,xs.Z)))
    int_points = int_points.dropna()
    int_points.index = range(len(int_points))
    int_points = int_points.iloc[int_points.round(1).drop_duplicates(subset=['CSID','Station']).index,:].reset_index(drop=True)

    # before we go any further lets clip the raster to the buffer of the XSs
    with rio.open(dem,'r') as src:
        masked_array, masked_transform = mask(src, shapes=[box(*xs.total_bounds).buffer(buffer)], crop=True, nodata=-9999, indexes=1)
        nd_mask = (masked_array==-9999)
        
        # get masked raster geo data
        masked_profile = src.meta.copy()
        masked_profile.update({
            "driver": "GTiff",
            "height": masked_array.shape[0],
            "width": masked_array.shape[1],
            "transform": masked_transform,
            "nodata": -9999})
           
    #create linear Rbf interpolator
    int_r,int_c = rio.transform.rowcol(masked_transform, int_points.geometry.x, int_points.geometry.y)
    rc = pd.DataFrame(np.array([int_c,int_r]).T,columns=['rows','cols']).drop_duplicates()
    rbfi = RBFInterpolator(rc.values, int_points.loc[rc.index,'Z'], kernel='linear')
    
    # interpolate REM zero elevation (wse) over cells within buffered mask
    ci,ri = np.meshgrid(np.arange(masked_array.shape[1]), np.arange(masked_array.shape[0]))
    ci = ci[~nd_mask]
    ri = ri[~nd_mask]
    
    int_wse = rbfi(np.stack([ci,ri]).T)
    wse = masked_array.copy()
    wse[~nd_mask] = int_wse
    
    rem = masked_array - wse
    
    if limits:
        rem = np.where((rem>limits[1]) | (rem<limits[0]),-9999,rem)
        
    rem[nd_mask] = -9999
    
    with rio.open(output,'w',**masked_profile) as dst:
        dst.write(rem,indexes=1)
            
    if wse_path:
        with rio.open(wse_path,'w',**masked_profile) as wse_dst:
            wse_dst.write(wse,indexes=1)
            
    print('\nREM created at {0}'.format(output))

def htab_1D(station,elevation,slope,D50,max_depth=10,breaks=None,save=None):
    station = np.array(station)
    elevation = np.array(elevation)
    
    twg = np.min(elevation)
    
    htab = pd.DataFrame([],columns=['d','wse','Q','u','n','S','A','P','R','n_chan'])
    
    for d in np.linspace(0.1,max_depth,25):
        wse = twg + d
        
        boo = (elevation<wse)
        
        if boo.all():
            print('Error - Unconfined XS at {0}'.format(round(wse,2)))
            continue
        
        indices = np.nonzero(boo[1:] != boo[:-1])[0] + 1
        #indices = np.array([i-1 if np.where(indices==i)[0]%2==0 else i+1 for i in indices])
        indices = np.array([i-1 if np.where(indices==i)[0]%2==0 else i for i in indices])
        
        if breaks:
            chan_ind = np.array([np.argmin(abs(station-bound)) for bound in breaks])
            chan_ind = np.delete(chan_ind,elevation[chan_ind]>wse)
            indices = np.sort(np.unique(np.concatenate([indices,chan_ind]).flatten()))
        
        sta = np.split(station, indices)
        sta = [s for s in sta if (elevation[np.searchsorted(station,s)]<wse).any()]
        sta = [np.append(s,station[np.argwhere(station==max(s))+1]) for s in sta]
        end_sta = [np.argwhere(station==s[-1]) for s in sta]
        
        elev = np.split(elevation, indices)
        elev = [e for e in elev if (e<wse).any()]
        elev = [np.append(e,elevation[end_sta[i]]) for i,e in enumerate(elev)]
        
        channels = [np.array([sta[i],elev[i]]).astype(float) for i in range(len(sta))]
        channels = [chan for chan in channels if chan.size>0]
        
        aas = []
        ps = []
        rs = []
        qs = []
        us = []
        ns = []
        for chan in channels:
            boo = (chan[1]<wse)
            
            if wse<chan[1,0]:
                chan[0,0] = interp1d(chan[1,:2],chan[0,:2])(wse)
            if wse<chan[1,-1]:
                chan[0,-1] = interp1d(chan[1,-2:],chan[0,-2:])(wse)
                
            chan[1,[0,-1]] = wse
    
            a = trapezoid(wse - chan[1],chan[0])
            p = np.sqrt(np.sum((chan.T[1:] - chan.T[:-1])**2, -1)).sum()
            
            r = a/p
            
            f = 8/(5.62*np.log10(a/(max(chan[0])-min(chan[0]))/D50)+4)**2
            n = (1.49/(8*32.17*r*slope/f)**(1/2))*r**(2/3)*slope**(1/2)
            if n > 0.2:
                n = 0.2
            
            u = (1.49/n)* r**(2/3) * slope**(0.5)
            q = a*u
            
            aas.append(a)
            ps.append(p)
            rs.append(r*q)
            qs.append(q)
            us.append(u*q)
            ns.append(n*q)
            
        htab.loc[len(htab)] = [d,wse,sum(qs),sum(us)/sum(qs),sum(ns)/sum(qs),slope,sum(aas),sum(ps),sum(rs)/sum(qs),len(channels)]

        
    if save:
        htab.to_excel(save)
    else:
        return htab
    
def htab_2D(rem,extents,vcl,slope,roughness,channel_area=None,channel_roughness=0.035,save=None):
    with rio.open(rem) as src:
        a = src.read(1)
        profile = src.profile.copy()
        
    if isinstance(extents,str):
        extents = gpd.read_file(extents).to_crs(profile['crs'])
    else:
        extents = extents.to_crs(profile['crs'])
        
    if isinstance(vcl,str):
        vcl = gpd.read_file(vcl).to_crs(profile['crs'])
    else:
        vcl = vcl.to_crs(profile['crs'])
        
    if channel_area:
        if isinstance(channel_area,str):
            channel_area = gpd.read_file(channel_area).to_crs(profile['crs'])
        else:
            channel_area = channel_area.to_crs(profile['crs'])
        
        channel_mask = rio.features.geometry_mask([channel_area.geometry.unary_union],a.shape,profile['transform'],invert=True)
    else:
        channel_mask = np.full(a.shape,True)
    
    px, py = np.gradient(a, profile['transform'][0])
    slope_surf = np.sqrt(px ** 2 + py ** 2)
    
    for i,row in extents.iterrows():
        mask = rio.features.geometry_mask([row.geometry],a.shape,profile['transform'],invert=True)
        mask = (mask & ~channel_mask)
        
        rel_arr = row.WSE - a
        
        ### CALCS for floodplain
        vol = rel_arr[mask].sum()*profile['transform'][0]**2
        A = vol/vcl.geometry.length.sum()
        
        surface_area = np.sqrt(slope_surf[mask]**2 + profile['transform'][0]**2).sum()
        P = surface_area/vcl.geometry.length.sum()
        
        if isinstance(slope,float):
            S = slope
        else:
            S = row[slope]
        
        FP_q = (1.49/roughness) * A * (A/P)**(2/3) * S**(0.5)
        
        ### CALCS for active channel
        if channel_area is not None:
            vol = rel_arr[channel_mask].sum()*profile['transform'][0]**2
            A = vol/vcl.geometry.length.sum()
            
            surface_area = np.sqrt(slope_surf[channel_mask]**2 + profile['transform'][0]**2).sum()
            P = surface_area/vcl.geometry.length.sum()
            
            AC_q = (1.49/roughness) * A * (A/P)**(2/3) * S**(0.5)
        else:
            AC_q = 0
        
        extents.loc[extents.index==i,'Q'] = FP_q + AC_q
        
        print('Q for RWSE of {0} = {1}'.format(round(row.WSE,2),round(FP_q + AC_q,0)))
    
    if save:
        extents.to_file(save)
    else:
        return extents
    
def pebble_count(photo_file, obj_color='yellow', obj_size_mm=190.5, min_area=50):        
    if isinstance(obj_color,str):
        obj_color = colors.to_rgba(obj_color)
    
    sam = sam_model_registry["vit_h"](checkpoint=r"Z:/Shared/W2r/Library/Python/sam_vit_h_4b8939.pth")
    mask_generator = SamAutomaticMaskGenerator(sam,
                                                points_per_side=64, 
                                                points_per_batch=32,
                                                pred_iou_thresh=0.7,
                                                stability_score_thresh=0.9,
                                                min_mask_region_area=min_area)
    
    with rio.open(photo_file) as src:
        image = src.read()
        image = image[:3,:,:]
        image = np.transpose(image, axes=[1,2,0])
        image = image.astype(np.uint8)
        
    masks = mask_generator.generate(image)
    
    def merge_masks(anns):
        sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)
        img = np.zeros((sorted_anns[0]['segmentation'].shape[0], sorted_anns[0]['segmentation'].shape[1]))
        for i,ann in enumerate(sorted_anns):
            m = ann['segmentation']
            img[m] = i+1
        return img
    
    img = merge_masks(masks)
    img = img.astype(int)
    
    props = regionprops_table(img, image, properties=('label', 'area', 'bbox', 'major_axis_length', 'minor_axis_length', 'intensity_mean'))
    grain_data = pd.DataFrame(props)
    grain_data[[col for col in grain_data.columns if 'intensity' in col]] = grain_data[[col for col in grain_data.columns if 'intensity' in col]]/255
    
    grain_data['closeness'] = np.abs(grain_data[[col for col in grain_data.columns if 'intensity' in col]] - obj_color[:3]).sum(axis=1)
    
    nb_label = grain_data.at[grain_data['closeness'].idxmin(), 'label']
    bbox = grain_data.loc[[grain_data['closeness'].idxmin()], ['bbox-1','bbox-0','bbox-3','bbox-2']].apply(lambda x: [i for i in x],axis=1).values[0]
    
    grain_data['pixel_size'] = obj_size_mm/grain_data.at[grain_data['closeness'].idxmin(), 'major_axis_length']
    grain_data['mm'] = grain_data['minor_axis_length']*grain_data['pixel_size']   
            
    grain_data['notes'] = np.nan
    grain_data.loc[grain_data.label==nb_label,'notes'] = 'Reference Obj'
    
    del grain_data['intensity_mean-0']
    del grain_data['intensity_mean-1']
    del grain_data['intensity_mean-2']
    del grain_data['closeness']
    
    grain_data.to_csv(photo_file.replace('.jpg','_grain_data.csv'),index=False)
    
    
    fig,ax = plt.subplots(2,1,height_ratios=[2,1],figsize=(10,8))
    ax[0].imshow(image)
    nb_img = np.where(img==nb_label,1,np.nan)
    img = np.where(img==nb_label,0,img)
    ax[0].imshow(img,alpha=0.5,cmap='tab20')
    ax[0].imshow(img==0,alpha=0.5,cmap='bone_r')  
    ax[0].imshow(nb_img,cmap='autumn')
    gpd.GeoDataFrame([],geometry=[box(*bbox)]).plot(ax=ax[0],ec='r',fc='None',lw=1.2)
    
    ax[0].tick_params(
        axis='both',          
        which='both',     
        bottom=True,      
        top=False,        
        labelbottom=False,
        labelleft=False) 
    
    
    bins = np.geomspace(0.1,1000,1000)
    counts, bin_edges = np.histogram(grain_data.mm, bins=bins, range=None, density=None, weights=grain_data.area)
    centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    
    ax[1].plot(centers,np.cumsum(counts)/sum(counts)*100,color='k')
    
    ax[1].set_xscale('log')
    ax[1].set_xlim(2,1000)
        
    ax[1].axvspan(2,4,color='k',alpha=0.25)
    ax[1].axvspan(8,16,color='k',alpha=0.25)
    ax[1].axvspan(32,64,color='k',alpha=0.25)
    ax[1].axvspan(128,256,color='k',alpha=0.25)
    ax[1].axvspan(512,1048,color='k',alpha=0.25)
    ax[1].text(2.83,99,'Very Fine\nGravel',va='top',ha='center')
    ax[1].text(5.66,99,'Fine\nGravel',va='top',ha='center')
    ax[1].text(11.3,99,'Medium\nGravel',va='top',ha='center')
    ax[1].text(22.6,99,'Coarse\nGravel',va='top',ha='center')
    ax[1].text(45.3,99,'Very Coarse\nGravel',va='top',ha='center')
    ax[1].text(90.5,99,'Small\nCobbles',va='top',ha='center')
    ax[1].text(181,99,'Large\nCobbles',va='top',ha='center')
    ax[1].text(362,99,'Small\nBoulders',va='top',ha='center')
    ax[1].text(724,99,'Large\nBoulders',va='top',ha='center')
    
    ax[1].text(0.99,0.65,'D84 = {0}'.format(grain_data.mm.quantile(0.84).round(1)),va='center',ha='right',transform=ax[1].transAxes)
    ax[1].text(0.99,0.5,'D50 = {0}'.format(grain_data.mm.quantile(0.5).round(1)),va='center',ha='right',transform=ax[1].transAxes)
    ax[1].text(0.99,0.35,'D16 = {0}'.format(grain_data.mm.quantile(0.16).round(1)),va='center',ha='right',transform=ax[1].transAxes)

    ax[1].set_xlabel('Grain Size (mm)')
    ax[1].set_ylabel('Percent Finer Than')
    ax[1].axhline(16,ls='--',c='k',lw=0.5)
    ax[1].axhline(50,ls='--',c='k',lw=0.5)
    ax[1].axhline(84,ls='--',c='k',lw=0.5)
    
    fig.tight_layout()
    
    fig.savefig(photo_file.replace('.jpg','_grain_labels.png'),dpi=400)
    
    print('{0} pebbles counted for {1}'.format(str(len(grain_data)),photo_file))
        
    