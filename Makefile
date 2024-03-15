# time period crime dataset
# author: James He
# date: 2024-03-12
# example usage: make all

# 'make all' will automatically create files targeted in all:
all: data/raw/raw_data.csv \
	data/processed/processed_data.csv \ 
	results/time_period_plot.png \
	results/records_by_time_and_day_plot.png \ 
	results/cross_validation_results.csv \
	results/crime_coefficients.csv \
	results/coefficients_of_lr_model_plot.png \
	reports/crime_report.html
	reports/crime_report.pdf

# download data
data/raw/raw_data.csv: src/script_raw.py 
	python src/script_raw.py \
	--out_type=csv \
	--url=https://data.sfgov.org/resource/wg3w-h783.csv?$query=SELECT%0A%20%20%60incident_datetime%60%2C%0A%20%20%60incident_date%60%2C%0A%20%20%60incident_time%60%2C%0A%20%20%60incident_year%60%2C%0A%20%20%60incident_day_of_week%60%2C%0A%20%20%60report_datetime%60%2C%0A%20%20%60row_id%60%2C%0A%20%20%60incident_id%60%2C%0A%20%20%60incident_number%60%2C%0A%20%20%60cad_number%60%2C%0A%20%20%60report_type_code%60%2C%0A%20%20%60report_type_description%60%2C%0A%20%20%60filed_online%60%2C%0A%20%20%60incident_code%60%2C%0A%20%20%60incident_category%60%2C%0A%20%20%60incident_subcategory%60%2C%0A%20%20%60incident_description%60%2C%0A%20%20%60resolution%60%2C%0A%20%20%60intersection%60%2C%0A%20%20%60cnn%60%2C%0A%20%20%60police_district%60%2C%0A%20%20%60analysis_neighborhood%60%2C%0A%20%20%60supervisor_district%60%2C%0A%20%20%60supervisor_district_2012%60%2C%0A%20%20%60latitude%60%2C%0A%20%20%60longitude%60%2C%0A%20%20%60point%60%2C%0A%20%20%60%3A%40computed_region_jwn9_ihcz%60%2C%0A%20%20%60%3A%40computed_region_jg9y_a9du%60%2C%0A%20%20%60%3A%40computed_region_h4ep_8xdi%60%2C%0A%20%20%60%3A%40computed_region_n4xg_c4py%60%2C%0A%20%20%60%3A%40computed_region_nqbw_i6c3%60%2C%0A%20%20%60%3A%40computed_region_viu7_rrfi%60%2C%0A%20%20%60%3A%40computed_region_26cr_cadq%60%2C%0A%20%20%60%3A%40computed_region_qgnn_b9vv%60%0AWHERE%20caseless_one_of(%60incident_year%60%2C%20%222023%22) \
	--out_file=data/raw/raw_data.csv

# processed data (these are the transformed data, ready to use for analysis)
data/processed/processed_data.csv: src/script_processed.py
	python src/script_processed.py \
	--input=data/raw/raw_data.csv \
	--out_file=data/processed/processed_data.csv

# EDA visualizations (the script for initial visualization of the dataset)
results/time_period_plot.png results/records_by_time_and_day_plot.png: src/eda_visualizations.py data/processed/processed_data.csv
	python src/eda_visualizations.py \
	--train=data/processed/processed_data.csv \
	--out_dir=results

# analysis (perform analysis, predicting on the processed data)
results/cross_validation_results.csv results/crime_coefficients.csv: src/analysis.py data/processed/processed_data.csv
	python src/analysis.py \
	--input=data/processed/processed_data.csv \
	--out_file=results/cross_validation_results.csv \ 
	--out_file=results/crime_coefficients.csv

# final visualization (visualization of the analysis)
results/coefficients_of_lr_model_plot.png: src/analysis_visualization.py data/processed/processed_data.csv
	python src/analysis_visualization.py \
	--train=data/processed/processed_data.csv \
	--out_dir=results

# render to html
reports/crime_report.html: results reports/quarto_reports.qmd
results/time_period_plot.png \
results/records_by_time_and_day_plot.png \ 
results/coefficients_of_lr_model_plot.png
	quarto render reports/quarto_reports.qmd --to html

# render to pdf
reports/crime_report.pdf: results reports/quarto_reports.qmd
	quarto render reports/qmd_example.qmd --to pdf

# 'make clean' will remove targeted files in clean:
clean:
	rm -f data
	rm -f results/cross_validation_results.csv \
	results/crime_coefficients.csv
	rm -f results/time_period_plot.png \
	results/records_by_time_and_day_plot.png \
	results/coefficients_of_lr_model_plot.png
	rm -rf reports/crime_report.html
	rm -rf reports/crime_report.pdf

