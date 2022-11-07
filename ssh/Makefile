D = "docker"
DC = "docker-compose"
# 適宜変えること
CONTAINER = "tenno-hai-ssh"
NAME=""

sh:
	$(D) exec -it $(CONTAINER) bash
up:
	$(DC) up -d
# # docker cp /tmp/local_file.php container_test1:/tmp/local_copy_file.php
# cp:
# 	$(D) cp ./tmp/test.py $(CONTAINER):./tmp/test.py
submit:
	$(D) stop $(CONTAINER)
	$(D) commit $(CONTAINER) $(NAME)/$(CONTAINER)
	$(D) push $(NAME)/$(CONTAINER)