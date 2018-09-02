.PHONY: clean

bst:
	@chmod 755 .
	@python ./bst.py

openhash:
	@chmod 755 .
	@g++ -o ./openhash.out ./openhash.cpp
	@./openhash.out

dijkstra:
	@chmod 755 .
	@g++ -o ./dijkstra.out ./dijkstra.cpp
	@./dijkstra.out

dfs:
	@chmod 755 .
	@python ./dfs.py

closedhash:
	@chmod 755 .
	@python3 ./closedhash.py

floyd:
	@chmod 755 .
	@python3 ./floyd.py

clean:
	@\rm -f ./*.pyc
	@rm -f ./*.out

