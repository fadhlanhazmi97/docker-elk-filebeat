FROM docker.elastic.co/kibana/kibana:7.1.1
COPY --chown=kibana:kibana kibana.yml /usr/share/kibana/config/
RUN ./bin/kibana-plugin install https://github.com/bitsensor/elastalert-kibana-plugin/releases/download/1.0.4/elastalert-kibana-plugin-1.0.4-7.1.1.zip
CMD ["kibana"]