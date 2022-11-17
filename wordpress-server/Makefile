D = "docker"
DC = "docker-compose"
# 適宜変えること
CONTAINER = "tenno-hai-wordpress"
NAME=""

sh:
	$(D) exec -it $(CONTAINER) bash
up:
	$(DC) up -d --build

down:
	$(DC) down

submit:
	$(D) stop $(CONTAINER)
	$(D) commit $(CONTAINER) $(NAME)/$(CONTAINER)
	$(D) push $(NAME)/$(CONTAINER)