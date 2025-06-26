This a folder of an example data set.

Data are collected in folders with the following schema

YYYYMMDD_XXin_target where XX refers to the telescope used and target is 
	usually the target observed or is sometimes what class  was collecting data.
20250624_14in_1998UB17


That folder will usually contain 3 subdirectories:
ancillary	-- contains starcharts, weather screenshots, extraneous test images showing focus, starfield. These are useful for analysis but not required.
calibration	-- contains the darks, bias, and flatfield calibration files needed for calibrating the data
	calib-yyy-bi.fit	file name schema for bias frames
	calib-yyy-d.fit		file name schema for dark frames
	flat-yyy-f.fit		file name schema for flatfields
	where yyy is frame number, bi is used to denote bias, d is used to denote darks, and f denotes the filter used
	
science		-- contains the science, aka raw or light, frames
	target-yyy-f.fit	file name schema for science frames
	where yyy is frame number, f denotes the filter used


and a log (text) file
XXin_YYYYMMDD_log.txt
14in_20250624_log.txt