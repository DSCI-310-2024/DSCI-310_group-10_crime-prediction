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
	docs/quarto_reports.html \
	docs/quarto_reports.pdf \
	docs/index.html
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
docs/quarto_reports.html: results docs/quarto_reports.qmd
	quarto render docs/quarto_reports.qmd --to html

# render to pdf
docs/quarto_reports.pdf: results docs/quarto_reports.qmd
	quarto render docs/quarto_reports.qmd --to pdf

# create index.html
docs/index.html: results docs/quarto_reports.qmd
	cp docs/quarto_reports.html docs/index.html

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
