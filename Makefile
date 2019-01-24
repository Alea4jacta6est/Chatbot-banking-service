TEST_PATH=./

interactive:
	python -m rasa_core.train interactive -s stories.md -d domain.yml -o models/dialogue --nlu models/current/nlu

train-nlu:
	python -m rasa_nlu.train -c config.yml --fixed_model_name_current --data nlu.md -o models/nlu

train-core:
	python -m rasa_core.train -s stories.md -d domain.yml -o models/dialogue --epochs 250

cmdline:
	python -m rasa_core.run -d models/dialogue -u models/nlu/default/current --debug

visualize:
	python -m rasa_core.visualize -s data/stories.md -d domain.yml -o story_graph.png

host:
	python -m rasa_nlu.server -c nlu_config.yml --path models/nlu --pre_load legal_model

activate_actions:
    python -m rasa_core_sdk.endpoint --actions actions

launch:
    python -m rasa_core.run --core models/dialogue --nlu models/nlu/legal_project/legal_model --endpoints endpoints.yml --enable_api


