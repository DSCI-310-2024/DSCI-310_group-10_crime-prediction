# time period crime dataset
# date: 2024-03-12

all: results/chart1.png results/chart2.png results/chart3.png results/processed.rds doc/time_period_crime_report.md

# download data
data/raw/raw_data_file.csv: src/script_raw.py 
	python src/script_raw.py \
	--out_type=csv \
	--url=https://data.sfgov.org/resource/wg3w-h783.csv?$query=SELECT%0A%20%20%60incident_datetime%60%2C%0A%20%20%60incident_date%60%2C%0A%20%20%60incident_time%60%2C%0A%20%20%60incident_year%60%2C%0A%20%20%60incident_day_of_week%60%2C%0A%20%20%60report_datetime%60%2C%0A%20%20%60row_id%60%2C%0A%20%20%60incident_id%60%2C%0A%20%20%60incident_number%60%2C%0A%20%20%60cad_number%60%2C%0A%20%20%60report_type_code%60%2C%0A%20%20%60report_type_description%60%2C%0A%20%20%60filed_online%60%2C%0A%20%20%60incident_code%60%2C%0A%20%20%60incident_category%60%2C%0A%20%20%60incident_subcategory%60%2C%0A%20%20%60incident_description%60%2C%0A%20%20%60resolution%60%2C%0A%20%20%60intersection%60%2C%0A%20%20%60cnn%60%2C%0A%20%20%60police_district%60%2C%0A%20%20%60analysis_neighborhood%60%2C%0A%20%20%60supervisor_district%60%2C%0A%20%20%60supervisor_district_2012%60%2C%0A%20%20%60latitude%60%2C%0A%20%20%60longitude%60%2C%0A%20%20%60point%60%2C%0A%20%20%60%3A%40computed_region_jwn9_ihcz%60%2C%0A%20%20%60%3A%40computed_region_jg9y_a9du%60%2C%0A%20%20%60%3A%40computed_region_h4ep_8xdi%60%2C%0A%20%20%60%3A%40computed_region_n4xg_c4py%60%2C%0A%20%20%60%3A%40computed_region_nqbw_i6c3%60%2C%0A%20%20%60%3A%40computed_region_viu7_rrfi%60%2C%0A%20%20%60%3A%40computed_region_26cr_cadq%60%2C%0A%20%20%60%3A%40computed_region_qgnn_b9vv%60%0AWHERE%20caseless_one_of(%60incident_year%60%2C%20%222023%22) \
	--out_file=data/raw/raw_data_file.csv

# porcessed data (these are the transformed data, ready to use for analysis)
data/processed/data_processed.csv: src/script_processed.py
	python src/script_processed.py \
	--input=data/raw/raw_data_file.csv \
	--out_file=data/processed/processed_data.csv

# EDA visualizations (the script for initial visualization of the dataset)
results/chart1.png results/chart2.png: src/script_eda.py data/processed/processed_data.csv
	python src/script_eda.py \
	--train=data/processed/processed_data.csv \
	--out_dir=results

# analysis (perform analysis, predicting on the processed data)
results/processed.rds: src/script_analysis.py data/processed/processed_data.csv
	python src/script_analysis.py \
	--train=data/processed/processed_data.csv \
	--out_dir=results

# Final visualizations (visualizations of the analysis)
 results/chart3.png: src/script_visual.py data/processed/processed_data.csv
	python src/script_visual.py \
	--train=data/processed/processed_data.csv \
	--out_dir=results

# render report
doc/time_period_crime_report.md: doc/time_period_crime_report.Rmd doc/time_period_crime_refs.bib
	python -e "rmarkdown::render('doc/time_period_crime_report.Rmd')"

clean:
	rm -rf data
	rm -rf results
	rm -rf doc/time_period_crime_report.md doc/time_period_crime_report.html

