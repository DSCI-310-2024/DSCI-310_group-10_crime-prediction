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
	reports/quarto_reports.html \
	reports/quarto_reports.pdf

# download data
data/raw/raw_data.csv: src/script_raw.py 
	python src/script_raw.py \
	https://data.sfgov.org/resource/wg3w-h783.csv \
	data/raw/raw_data.csv

# processed data (these are the transformed data, ready to use for analysis)
data/processed/processed_data.csv: src/script_processed.py data/raw/raw_data.csv
	python src/script_processed.py \
	data/raw/raw_data.csv \
	data/processed/processed_data.csv

# EDA visualizations (the script for initial visualization of the dataset)
results/time_period_plot.png results/records_by_time_and_day_plot.png: src/eda_visualizations.py data/processed/processed_data.csv
	python src/eda_visualizations.py \
	data/processed/processed_data.csv \
	results

# analysis (perform analysis, predicting on the processed data)
results/cross_validation_results.csv results/crime_coefficients.csv: src/analysis.py data/processed/processed_data.csv
	python src/analysis.py \
	data/processed/processed_data.csv \
	results

# final visualization (visualization of the analysis)
results/coefficients_of_lr_model_plot.png: src/analysis_visualization.py results/crime_coefficients.csv
	python src/analysis_visualization.py \
	results/crime_coefficients.csv \
	results

# render to html
reports/quarto_reports.html: results reports/quarto_reports.qmd
	quarto render reports/quarto_reports.qmd --to html

# render to pdf
reports/quarto_reports.pdf: results reports/quarto_reports.qmd
	quarto render reports/quarto_reports.qmd --to pdf

# 'make clean' will remove targeted files in clean:
clean:
	rm -rf data/raw/raw_data.csv
	rm -rf data/processed/processed_data.csv
	rm -rf results/cross_validation_results.csv \
		results/crime_coefficients.csv\
		results/dummy_results.csv
	rm -rf results/time_period_plot.png \
		results/records_by_time_and_day_plot.png \
		results/coefficients_of_lr_model_plot.png
	rm -rf docs/quarto_reports.html \
		docs/quarto_reports.pdf
	rm -rf docs/index.html


