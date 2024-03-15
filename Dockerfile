FROM quay.io/jupyter/scipy-notebook:2024-02-24

  RUN conda install -y altair=5.2.0 \
     altair_saver=0.1.0 \
     click=8.1.7 \
     numpy=1.26.4 \
     pandas=2.2.1 \
     scikit-learn=1.4.1.post1 \
     pytest=8.1.1 \
     vl-convert-python-1.3.0